# VOYAGE VISTA
Voyage Vista is an advanced app that revolutionizes multimodal trip planning by integrating various public transportation apps into a cohesive platform. This innovative tool allows users to efficiently plan journeys by seamlessly combining options like buses, trains, auto metro, ride-sharing vehicles, and bike rentals. What sets Voyage Vista apart is its ability to customize routes based on individual preferences such as travel time, cost considerations, and environmental impact, ensuring journeys are optimized for efficiency and user satisfaction. The app provides real-time updates on transit schedules, ride availability, and bike station locations, enabling smooth transitions between different modes of transportation. By centralizing these features, Voyage Vista enhances user convenience and promotes sustainable travel choices, offering a comprehensive solution to urban mobility challenges by leveraging technology to simplify and improve the way people navigate cities.

## Team members
1) Harigovind P
2) Pavithra
3) Seetha lakshmi
4) Sreehari S

## How it Works ?
The described system is a comprehensive travel route optimizer designed to enhance the efficiency and experience of daily commuting by integrating various transport modes. By combining options such as buses, trains, ride-sharing, and biking, it allows users to plan trips using a mix of these modes, ensuring the most efficient and effective route for their specific needs. The system minimizes travel time and enhances productivity by analyzing different transport options and their schedules to identify the quickest routes, saving users valuable time. It caters to a wide range of users, including those needing disability-friendly routes and cyclists, ensuring accessible and safe travel for all.
Furthermore, the system helps users find cost-effective travel options, significantly reducing their overall travel expenses by comparing the costs of different transport modes and suggesting affordable yet efficient combinations. By encouraging the use of public transport and alternative modes like biking and ride-sharing, the system alleviates urban congestion, improves traffic flow, and reduces commuting stress. It also promotes sustainable travel choices, lowering carbon emissions and supporting urban sustainability efforts. This optimizer not only makes daily travel more efficient and cost-effective but also contributes to reducing congestion and enhancing urban sustainability.

## Libraries used
- pymysql - 1.1.1
- tkinter - 0.0.9
- PIL - 1.1.0
- datetime - 5.5
- smtplib - 0.0.1

## How to configure
**GUI Element Configuration Overview**
This explanation outlines the core principles behind configuring elements in a graphical user interface (GUI) using a Python library (likely Tkinter).

**Window Properties**
1. **Title:** Set the window title for display in the title bar.
2. **Resizability:** Enable/disable window resizing.
3. **Geometry:** Define the window size (width x height) and initial position on the screen.
4. **Icon:** Set a custom icon image for the window.
5. **Background Color:** Define the background color for the main window area.

**Widget Placement and Configuration**
- **Frames:** Used to organize and group other widgets within the window.
  - Placement: Techniques like `place` and `pack` are used to position frames within the window.
  - Configuration: Background color can be set for frames.
- **Labels:** Display text elements for information or instructions.
  - Placement: Similar to frames, placement techniques like `place` and `pack` are used.
  - Configuration: Font, text color, and background color can be customized.
- **Buttons:** Interactive elements that trigger actions when clicked.
  - Placement: Techniques like `place` are used to position buttons.
  - Configuration: Font, text color, background color, button style (raised, etc.), and action commands are defined.
- **Footers:** Often frames used to display information at the bottom of the window.
  - Placement: Typically packed at the bottom of the window using `pack` with `side=tk.BOTTOM`.
  - Configuration: Background color can be set for footers.
- **Text Fields:** Allow users to enter text input.
  - Placement: Techniques like `grid` can be used for precise layout within frames.
  - Configuration: Font, text color, and background color can be customized.

**Additional Considerations**
- **Layout Managers:** Techniques like `grid` and `pack` help arrange widgets within frames.
- **Event Handling:** Functions can be assigned to buttons to define their behavior when clicked.
- **Appearance:** Font, color, and styling options are used to create a visually appealing interface.

**Benefits of Abstraction**
This abstract explanation avoids code-specific details and focuses on general concepts. This makes it easier to understand and apply the principles to different GUI libraries or programming languages.

## How to Run
Before running the code, it's essential to understand its structure:
Imports: Imports necessary libraries like tkinter for GUI creation, messagebox for displaying messages, pymysql for database interaction (if used), and potentially PIL for image handling.
Class Definitions: Defines classes like TripPlannerWindow and Login to encapsulate GUI components and logic.
Function Definitions: Contains functions for various tasks like button clicks, database operations, and email sending.
Main Execution Block: Typically found at the end of the file, using if __name__ == '__main__': to control when the code runs.
Running the Code
Save the Code: Save the code as a Python file (e.g., voyage_vista.py).
Install Required Libraries: Ensure you have the necessary libraries installed. Open a terminal or command prompt and use pip install tkinter messagebox pymysql PIL (if needed).
Run the Script:
Using a Python IDE: Open the Python file in an IDE like PyCharm, Visual Studio Code, or IDLE and run it directly.
Command Line: Open a terminal or command prompt, navigate to the directory where the file is saved, and run python voyage_vista.py.
Additional Considerations
Database Connection: If you're using a database, make sure you have the correct database credentials and the database is set up.
Image Files: Ensure the image files (e.g., voyage_vista_icon.png) are in the same directory as the Python script or provide the correct path.
Email Configuration: If sending emails, configure the email settings correctly.

## Output
![Screenshot 2024-07-27 042252](https://github.com/user-attachments/assets/e510566b-93f2-47a5-ad4a-796673d8b928)
![Screenshot 2024-07-27 042312](https://github.com/user-attachments/assets/40b753db-ced1-42af-b115-4db2d6f778a5)
![Screenshot 2024-07-27 042451](https://github.com/user-attachments/assets/0aea1dd9-e427-438e-9d62-72ef9689bfca)
![Screenshot 2024-07-27 042514](https://github.com/user-attachments/assets/ffeea7c9-5dd5-4a10-894e-43c3e133e49c)
![Screenshot 2024-07-27 042918](https://github.com/user-attachments/assets/85e09993-91a6-4e21-9eb2-8b81939aab0c)
![Screenshot 2024-07-27 042951](https://github.com/user-attachments/assets/5f360871-827a-4c84-8b10-c3f13d4e4250)
![Screenshot 2024-07-27 043010](https://github.com/user-attachments/assets/6320265f-ffe3-4c55-a10a-8e1a9a9f48d5)
