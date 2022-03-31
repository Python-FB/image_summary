# image_summary
Application to generate a text summary of a given image


## Project Plan

#### Front End
    - Browser-based
    - Drag-and-drop images files
    - Browse the local file system for image
    - Display results from ML Engine
#### Back End
    - Verify user input
        - If user input is invalid, return error to front end
    - If user input is valid
        - Pass input to ML Engine
        - ML Engine processes image
            - Image contents are translated to text object
            - Text is converted to audio object
        - ML output is sent back to Front End