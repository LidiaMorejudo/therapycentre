This will be my Read

# 🌿 Therapy Centre – Holistic Yoga in the Heart of Bristol

Therapy Centre is a serene and beautifully designed wellness resort located in the heart of Bristol, dedicated to holistic yoga therapy. This full-stack web application enables users to seamlessly explore and engage with the centre’s services.

Through the website, users can:

- Book personalized yoga therapy sessions

- Browse a detailed price list

- Learn more about experienced practitioners

- Contact the centre directly

Access essential information, including location and directions

Built using the Django framework, this platform provides full CRUD functionality, allowing users to create, read, update, and delete their session bookings with ease.

**IMAGES OF THE DEPLOYED SITE WILL GO HERE**

Images were sourced from [AmiResponsive](https://amiresponsive.co.uk/)

## Table of content
- [UX/UI Design](#uxui-design)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Colour scheme](#colour-scheme)
  - [Project Planning](#project-planning)
    - [Agile methodologies](#agile-methodologies)
    - [Database design](#database-design)
- [Features](#features)
  - [Existing features](#existing-features)
  - [Header](#header)
  - [Navigation menu](#navigation-menu)
  - [Landing page](#landing-page)
  - [Location page](#location-page)
  - [Contact page](#contact-page)
  - [Book a table page](#book-a-table-page)
  - [Register account/login page](#register-accountlogin-page)
  - [Footer](#footer)
  - [Potential future features](#potential-future-features)
- [Technologies used](#technologies-used)
  - [Languages](#languages)
  - [Database](#database)
  - [Frameworks](#frameworks)
  - [Libraries & Additional Programs/Software/Tools](#libraries--additional-programssoftwaretools)
- [Manual Testing](#manual-testing)
  - [Responsivness](#responsivness)
  - [Browser compability](#browser-compability)
  - [Validator testing](#validator-testing)
  - [User Story testing](#user-story-testing)
  - [Bugs](#bugs)
- [Deployment](#deployment)
  - [Forking](#forking)
  - [Cloning](#cloning)
  - [Deployment to Heroku](#deployment-to-heroku)
- [References/credit](#referencescredit)
  - [Content](#content)
  - [Media](#media)

## UX/UI Design

### User Stories

**EPIC 1: Book a Session**

As a **Site User**, I can book a session at the therapy centre online so that I can choose a date, time, and type of session that suits me.

As a **Site User**, I want the booking process to be simple and intuitive so that I can complete a booking with ease.

As a **Site User**, I can provide specific information (e.g., special requirements) so that the therapist is aware in advance.

As a **Site User**, I can receive an email confirmation of my booking so that I can refer back to the details later.

As a **Site User**, I can view the therapy centre’s booking policy before submitting the form so that I know what to expect.

As a **Site Admin**, I can view all upcoming bookings by day, week, or month so that I can ensure sessions are properly scheduled and staffed.

**EPIC 2: Manage Bookings**

As a **Site User**, I can register an account so that I can view and manage my bookings online.

As a **Site User**, I can log in to my account from any device so that I can access or update my bookings at any time.

As a **Site User**, I can edit or cancel my bookings online so that I can adjust them if my plans change.

As a **Site User**, I can delete my bookings myself so that I don’t need to contact the therapy centre to make changes.

As a **Site User**, I can view the total number of clients booked per session so that I can manage capacity effectively.

As a **Site Admin**, I can modify bookings through the admin panel in case a client needs assistance updating their booking.

**EPIC 3: Contact the Therapy Centre**

As a **Site User**, I can easily find the therapy centre’s contact details so that I can reach out with questions or special requests.

As a **Site User**, I can view the therapy centre’s opening hours so that I know the best times to contact them.

As a **Site User**, I can fill out a contact form so that I can send inquiries without having to call or email separately.

As a **Site Admin**, I can view all incoming messages from the contact form so that I can respond promptly.

**EPIC 4: Locate the Therapy Centre**

As a **Site User**, I can find information about the therapy centre’s address so that I know where it is located.

As a **Site User**, I can view a map of the therapy centre’s location so that I can navigate there by car, public transport, or on foot.

**EPIC 5: View Available Sessions**

As a **Site User**, I can view a list of available sessions so that I can decide which one I would like to attend.

As a **Site Admin**, I can easily update session details and pricing so that clients always have accurate, up-to-date information.

**EPIC 6: Reviews**

As a **Site User**, I can write a review of the therapy centre so that others can learn from my experience.

As a **Site User**, I can read reviews from previous clients so that I can make an informed decision about booking a session.

As a **Site Admin**, I can moderate and respond to reviews so that feedback is managed professionally and constructively.

### Wireframes

Wireframes for both mobile devices and larger screens (such as tablets and desktop computers) were created using **Balsamiq and Microsoft Word**. The goal was to maintain a clean and straightforward design, with nearly every view having its own dedicated wireframe. This approach streamlined the development process, as the layout and structure were already clearly defined.

I thoroughly enjoyed working on this stage of the project. While a few adjustments were made during development—particularly to improve responsiveness—I decided to keep all original wireframes unchanged as a reference to the initial design vision.

**Examples**

The first example below showcases the landing page as viewed on a desktop browser or large tablet. It highlights the navigation bar with all menu items visible, a prominent header image (jumbotron), and what I consider the two most essential buttons for a therapy’s website from a user perspective.

![printscreen](/static/wireframes/main_landing_page.png)

These wireframes illustrate the mobile layout, designed to be clean and intuitive. A dropdown menu replaces the traditional navigation bar to maximize screen space, keeping the focus on the jumbotron, booking, and menu sections.

![printscreen](/static/wireframes/wireframes_mobiles_contactpage.png)

For a complete overview of the project’s wireframes, please refer to the dedicated documentation. The main README provides only a brief visual summary to maintain clarity and brevity. To explore all wireframe designs, including detailed layouts, click the link below:

[View Full Wireframes](docs/wireframes.md)

### Colour scheme

The website uses a calm and natural colour palette to create a soothing and welcoming atmosphere appropriate for a therapy centre. The primary background colour is a soft, muted green (#d9e8cc), chosen to evoke feelings of calmness and peace. Buttons and interactive elements use Bootstrap’s neutral grey tones to maintain a clean, professional appearance without clashing with the primary background. Social media icons are styled in black for clear visibility and a minimalist aesthetic. This colour scheme aims to provide a gentle and reassuring user experience, reinforcing the centre’s commitment to comfort and care.

![printscreen](/static/images/ColourScheme.png)

### Project planning


### Agile methodologies

Agile Methodologies in My Project

Excel Planning Board – I used Excel to plan and organize the Yoga Therapy Centre project. Each issue was written as a User Story with clear Acceptance Criteria. To make sure I understood the scope of each story, I also broke them down into smaller tasks. Along the way, I had to revisit the sheet, refine, and add new User Stories. This process highlighted for me the value of an iterative Agile approach.

The User Stories helped me stay focused on ensuring the essential functionality of the site came first, with design as an enhancement rather than the main priority.

Epics – I see the value of Epics in larger projects, since they give a clearer overview of related User Stories and help with prioritization. For a project of this size, Epics might be more than necessary, but the structure still helps me organize my work and thinking.

MoSCoW Prioritization – To keep priorities clear, each User Story was categorized using the MoSCoW methodology:

Must Have: Essential features required for the Yoga Therapy Centre website to function and serve its core purpose.

Should Have: Important features that add value but are not critical for basic functionality.

Could Have: Nice-to-have features that can be developed if time and resources allow.

Won’t Have (this time): Features intentionally left out of this version but considered for possible future development.


![printscreen](/static/images/agile.png)

An important note: some features that I consider essential for a Yoga Therapy Centre’s website and booking system (and therefore labeled as Must Have) were not implemented in this iteration. They didn’t even reach the “In Progress” stage in Excel. This was intentional, as my main focus for this project is on building a smooth and supportive user experience for clients. Administrative and back-office functionality is something I would be very interested in exploring in future versions of the project.


## Features

### Existing features


## Technologies used

### Languages
- HTML5
- CSS3
- JavaScript
- Python

### Libraries & Additional Programs/Software/Tools

- [Deep Dream Generator](https://deepdreamgenerator.com/) - I utilized Deep Dream Generator, an AI-powered tool, to create images for my project.