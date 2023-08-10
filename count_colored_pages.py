def count_colored_pages(pdf_path, output_file):
    """
    Disclaimer : This script was generated using bing chat to count the number of coloured pages of a thesis.
    
    Counts the number of colored pages in a PDF file and saves the results to a text file.
    
    This function takes the path to a PDF file and an output text file as input. It uses the `pdf2image` library to convert the PDF into a list of images, one for each page. It then loops through each page and checks if it is colored by splitting the image into its RGB channels and checking if they are all equal (which would indicate a grayscale image). If the page is not grayscale, it is counted as a colored page. The final count of colored pages, as well as the number of black and white pages and total pages, are saved to the specified text file.
    
    Args:
        pdf_path (str): The path to the PDF file to process.
        output_file (str): The path to the text file where the results should be saved.
    
    Returns:
        None
    
    Example:
        # Count colored pages in example.pdf and save results to results.txt
        pdf_path = 'example.pdf'
        output_file = 'results.txt'
        count_colored_pages(pdf_path, output_file)
    """
    # Convert PDF to images
    images = convert_from_path(pdf_path)
    
    # Initialize count of colored pages
    colored_pages = 0
    
    # Loop through each page
    for image in images:
        # Convert image to numpy array
        img = np.array(image)
        
        # Check if image is grayscale
        if len(img.shape) == 2 or img.shape[2] == 1:
            continue
        
        # Split image into RGB channels
        r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
        
        # Check if image is colored
        if not np.all(r == g) or not np.all(g == b):
            colored_pages += 1
    
    # Calculate number of black and white pages
    bw_pages = len(images) - colored_pages
    
    # Save results to text file
    with open(output_file, 'a') as f:
        f.write(f'{pdf_path}: {colored_pages} colored pages, {bw_pages} black and white pages, {len(images)} total pages\n')

# Example usage
pdf_path = 'example.pdf'
output_file = 'results.txt'
count_colored_pages(pdf_path, output_file)
