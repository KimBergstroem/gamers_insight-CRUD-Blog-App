README

# Gamers Insight

Gamers Insight is a dynamic web application tailored for gaming enthusiasts, providing a platform to share and explore in-depth reviews of various video games. With Gamers Insight, users can create detailed blog posts to analyze game mechanics, graphics, storylines, and overall experiences. The application offers a seamless interface for readers to discover and engage with diverse gaming perspectives, while also fostering a community that appreciates thoughtful game critiques. Whether you're a passionate gamer or simply curious about the latest releases, Gamers Insight offers a space to immerse yourself in comprehensive game reviews and discussions.

![]()
Developer: Kim Bergström <br>
[Live webpage]()

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
3. [Database](#database)
    1. [User App](#user-app)
    2. [Gamers Blog App](#Gamersblog-app)
4. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colour](#colours)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Wireframes](#wireframes)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks](#frameworks)
    3. [Database](#database)
    4. [Tools](#tools)
    5. [Supporting Libraries and Packages](#supporting-libraries-and-packages)
6. [Methodology](#methodology)
    1. [Agile Project Management with GitHub Projects](#agile-project-management-with-github-projects)
    2. [User Stories as GitHub Issues](#user-stories-as-github-issues)
    3. [Bug Tracking](#bug-tracking)
    4. [Iterative Development Approach](#iterative-development-approach)
    5. [Backlog and Subsequent Iterations](#backlog-and-subsequent-iterations)
7. [Features](#features)
    1. [Landing Page](#landing-page)
    2. [Gamers Blog Pages](#gamersblog-pages)
    3. [Review Pages](#review-pages)
    4. [User Account Management](#user-account-management)
    5. [Blog Management](#Blog-management)
    6. [Navigation](#navigation)
    7. [Future Features](#future-features)
8. [Testing](#testing)
9. [Bugs](#bugs)
    1. [Known bugs](#known-bugs)
    2. [Fixed bugs](#fixed-bugs)
10. [Deployment](#deployment)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

## Project Goals

Gamers Insight is a Django web application aimed at creating a vibrant platform for gamers to share their insights, opinions, and experiences about various games. The key objectives of the project include:

- **Empowering Gamers:** Providing a dedicated space for gamers to contribute their reviews, articles, and discussions about different games.
- **User-Centric Experience:** Offering users an engaging and intuitive interface that encourages exploration and interaction.
- **Content Organization:** Enabling users to categorize and manage their articles, reviews, and discussions effectively.
- **User Profiles:** Allowing users to create personalized profiles, showcase their gaming preferences, and keep track of their contributions.
- **Interactive Engagement:** Facilitating user interactions through comments, reviews, and discussions to foster a sense of community.
- **Administrator Control:** Equipping administrators with the tools to manage user accounts, moderate content, and ensure a safe environment.
- **Analytics and Insights:** Implementing analytics to understand user engagement, popular content, and areas for improvement.

### User Goals
- Exploring and sharing detailed game reviews and articles.
- Personalizing their profiles to showcase their gaming interests.
- Engaging in discussions and leaving comments to contribute to the gaming community.
- Saving favorite articles and reviews for easy access.
- Submitting their own game reviews, articles, and insights.
- Receiving notifications about new content and discussions.

### Site Owner Goals
- Providing a platform for gamers to express their thoughts and insights.
- Curating a diverse range of gaming-related content to cater to different preferences.
- Fostering a thriving gaming community where users can connect and share experiences.
- Ensuring user-generated content is moderated for quality and appropriateness.
- Enhancing user engagement and interaction through intuitive design and features.

Your project "Gamers Insight" aims to create a dynamic hub for gamers to connect, share, and explore the world of gaming through insightful articles, discussions, and reviews.

[Back up](#table-of-content)

## User Experience

### Target Audience
Gamers Insight is designed for the following target audience:

- Gaming enthusiasts and gamers looking for insights and reviews about various games.
- Individuals interested in exploring diverse gaming experiences and genres.
- Users who want to share their own game reviews, opinions, and experiences.
- Players seeking a platform to engage in discussions about their favorite games.
- Individuals who wish to stay updated with the latest gaming trends and discussions.

By catering to the interests and needs of gamers, Gamers Insight aims to become a hub for gaming enthusiasts to connect, share, and explore the gaming world.

### User Requirements and Expectations
When using Gamers Insight, users can expect the following features and characteristics to fulfill their needs:

- A user-friendly interface that provides intuitive navigation and easy access to gaming content.
- High-quality game reviews and articles that offer detailed insights and opinions.
- Responsive design ensuring a visually appealing experience across different devices.
- Personalized features, such as user profiles to showcase gaming preferences and track contributions.
- Interactive engagement through comments and discussions, fostering a sense of community.
- Notifications for new content and discussions to keep users informed and engaged.

Gamers Insight strives to create an immersive and interactive environment for users to share, discover, and discuss their passion for gaming.

[Back up](#table-of-content)

### User Stories

#### Epic 1: User Experience (Visitor)

- [Easily Navigate and Find Content (should-have)](https://github.com/KimBergstroem/PP4/issues/1)
- [Visually Appealing Homepage (should-have)](https://github.com/KimBergstroem/PP4/issues/2)
- [Search for Specific Games or Topics (could-have)](https://github.com/KimBergstroem/PP4/issues/3)
- [Read Detailed Game Reviews (should-have)](https://github.com/KimBergstroem/PP4/issues/4)
- [Create a Personalized Profile (should-have)](https://github.com/KimBergstroem/PP4/issues/5)
- [Save Favorite Articles and Create Reading Lists (should-have)](https://github.com/KimBergstroem/PP4/issues/6)

#### Epic 2: User Engagement and Interaction (Registered User)

- [Receive Notifications (could-have)](https://github.com/KimBergstroem/PP4/issues/7)
- [Leave Comments and Engage in Discussions (must-have)](https://github.com/KimBergstroem/PP4/issues/8)
- [Submit Own Articles and Reviews (must-have)](https://github.com/KimBergstroem/PP4/issues/9)
- [Edit or Delete Own Articles and Comments (must-have)](https://github.com/KimBergstroem/PP4/issues/10)
- [Earn Badges or Rewards (won't-have)](https://github.com/KimBergstroem/PP4/issues/11)

#### Epic 3: Administration and Content Management (Admin/Content Moderator)

- [Full Control Over User Accounts (must-have)](https://github.com/KimBergstroem/PP4/issues/12)
- [Review and Edit User-Submitted Articles (must-have)](https://github.com/KimBergstroem/PP4/issues/13)
- [Manage and Categorize Articles (could-have)](https://github.com/KimBergstroem/PP4/issues/14)
- [Track User Engagement and Analytics (could-have)](https://github.com/KimBergstroem/PP4/issues/15)

[Back up](#table-of-content)

## Database


### User App

### Gamers Blog App


## Design


### Design Choices

### Colour


### Fonts


### Structure


#### Before Logged In:

- **Landing Page** 
- **About Page:** 
- **Sign Up Page:** 
- **Login Page:** 

#### When Logged In:


#### Profile Navigation:


### Wireframes

## Technologies Used

### Languages
- HTML
- CSS
- Python

### Frameworks
- Django: A high-level Python web framework used for building the Gamers Insight Blog webbapplication.
- Crispy Forms: A Django package used for rendering forms in a more efficient and customizable way.
- Bootstrap v5.0: A popular CSS framework used for creating responsive and visually appealing user interfaces.
- Cloudinary: A cloud-based media management platform used for storing and serving images in the Blog Collective project.
- 
### Database
- ElephantSQL: ElephantSQL is a PostgreSQL database as a service. It is used as the database for the Blog Collective project, providing a reliable and scalable storage solution for the application's data.

### Tools


### Supporting Libraries and Packages


## Methodology

The Gamers Insight project follows a methodology inspired by agile principles, fostering collaboration, flexibility, and gradual development. The outlined approach has guided the project's evolution:

### Agile Project Management with GitHub Projects
To streamline project management, GitHub Projects is employed as a central hub. User stories and tasks are structured as GitHub issues, creating an organized workflow. The GitHub project board serves as a visual representation, tracking progress effectively.

### User Stories as GitHub Issues
Transforming user stories into GitHub issues captures user-centric functionalities. These issues interlink with respective user stories, simplifying access to criteria, tasks, and discussions.

### Bug Tracking for Seamless Development
Bugs uncovered during development are documented as GitHub issues, offering insights into each bug's characteristics, impact, and reproduction steps. By hyperlinking these issues in the README.md, users can stay updated on bug resolutions and contribute insights.

### Iterative Development Approach
The Gamers Insight project adheres to an iterative development approach, facilitating continuous enhancements within a predefined timeline. Despite its condensed schedule, the project accommodates future iterations and expansions.

### Future Backlog and Progress
The project board efficiently manages user stories, with the "Not started" column representing upcoming iterations. This backlog previews user stories set for subsequent development phases.

Emphasizing that the project timeline is expedited, the iterative approach maintains adaptability, enabling ongoing refinements and improvements aligned with evolving user needs.

For a comprehensive view of the project's trajectory, user stories, and bug tracking, explore the [Kanban board]([https://github.com/users/YourGitHubUsername/projects/your_project_number](https://github.com/users/KimBergstroem/projects/8/views/1)).

[Back up](#table-of-content)
 

## Features
### Landing Page:

### Review Pages:


### Blog Pages:


### User Account Management:


### Management:


### Navigation:


#### Unauthorized users


#### Unauthorized users


### Future Features


## Testing


## Bugs

### Known bugs



### Fixed bugs 


## Deployment


## Credits


### Media


### Django Documentation:


### W3 Schools:


### Stackoverflow:


### Geeksforgeeks: 


### Various tutorials and YouTube channels:


### Other open-source projects and packages:


## Acknowledgements

