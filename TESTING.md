# Gamers Insight Testing 

![Gamers Insight viewed in different screens](/docs/test.md/test.md-hero-image.png)

Developer: [Kim Bergström](https://github.com/KimBergstroem) <br>
[Live webpage](https://game-insight-1cff11f2b2d5.herokuapp.com/)<br>
[Project Repository](https://github.com/KimBergstroem/PP4)<br>



## CONTENTS

* [**Automated Testing**](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [JavaScript Validator](#javaScript-validator)
  * [PEP8 Validator](#javaScript-validator)
  * [Lighthouse](#lighthouse)
  * [Wave Accessibility Test](#wave)
* [**Manual Testing**](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Code Validation

### HTML Validation

W3C Markup Validation is a service offered by the W3C, which enables you to assess the compliance of your HTML code with the official standards. This service identifies syntax errors, improper tag usage, and other issues that might impact the structure and meaning of your web pages. By utilizing W3C Markup Validation, you can ensure that your HTML code is well-structured and conforms to established web standards.

Google Chrome web browser and the 'Inspect' function were used to capture the HTML page from our template, which was then validated against the W3C Validator.

In this project, a rich text editor called "Summernote" are used to allow users to create and update posts with HTML content. While Summernote enhances the user experience, it introduces some complexities when validating our HTML code.

When users create or update posts, they have the flexibility to input HTML, which can sometimes lead to unconventional HTML structures or attributes. These unconventional structures are detected as errors when we validate our HTML code using external tools like the W3C validator.

Due to the interaction between Summernote and the need to ensure the security of our application. To protect against security threats and potential attacks, we've implemented safeguards such as using the '|safe' filter in our forms. This filter prevents user-entered HTML from compromising the security of our application.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|landing_page.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-landing_page.png)</details>| ✅
|about.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-about.png)</details>| ✅
|login.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-login.png)</details>| ✅
|signup.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-signup.png)</details>| ✅
|index.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-index.png)</details>| ✅
|post_detail.html| "The font element is obsolete. Use CSS instead." | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-post_detail.png)</details>| ✅
|contactus.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-contactus.png)</details>| ✅
|contactus_success.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-contact-success.png)</details>| ✅
|profile.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-profile.png)</details>| ✅
|my_articles.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-myarticles.png)</details>| ✅
|post_create.html| Bad value true for attribute hidden on element textarea., Attribute cols not allowed on element div at this point.,  Bad value 100% for attribute width on element iframe: Expected a digit but saw % instead., The frameborder attribute on the iframe element is obsolete. Use CSS instead.  | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-post_create.png)</details>| ✅
|logout.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-logout.png)</details>| ✅
|post_delete.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-post_delete.png)</details>| ✅
|post_update.html| Bad value true for attribute hidden on element textarea., Attribute cols not allowed on element div at this point.,  Bad value 100% for attribute width on element iframe: Expected a digit but saw % instead., The frameborder attribute on the iframe element is obsolete. Use CSS instead. | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-post_update.png)</details>| ✅
|profile_delete.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-profile_delete.png)</details>| ✅
|profile_update.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-profile_update.png)</details>| ✅
|password_change.html| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-password_change.png)</details>| ✅

### CSS Validation
[W3C Jigsaw](https://jigsaw.w3.org/css-validator/) is a tool provided by the World Wide Web Consortium (W3C) that allows you to validate and check the correctness of your HTML and CSS code. It helps ensure that your web pages comply with the standards set by the W3C, promoting interoperability and accessibility.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|CSS file | No errors |<details><summary>Screenshot of result</summary>![Result](/docs/test.md/wc3/test-wc3-style.png)</details>| ✅
|Whole webpage | No errors  |[Result](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgame-insight-1cff11f2b2d5.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv#warnings)| ✅

### **PEP8 Validator** 
[PEP 8](https://pep8ci.herokuapp.com/) serves as a comprehensive style guide for writing Python code, emphasizing consistency and readability as its core principles. It offers guidance on code formatting, variable and function naming conventions, and various best practices. Adhering to PEP 8 principles contributes to enhancing code quality, making it more readable and maintainable.

Within the settings file, one URL was identified as being excessively long. The other lines that exceeded the recommended length were automatically generated by Django. All other files were free from errors and issues.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|game_insight/settings.py | All clear, no errors found |![Result](/docs/test.md/pep8/test-pep8-settings.png) | ✅
|game_insight/urls.py | All clear, no errors found |![Result](/docs/test.md/pep8/test-pep8-project-urls.png)| ✅
|blog/models.py | All clear, no errors found |![Result](/docs/test.md/pep8/test-pep8-models.png)| ✅
|blog/views.py | All clear, no errors found |![Result](/docs/test.md/pep8/test-pep8-views.png)| ✅
|blog/forms.py | All clear, no errors found |![Result](/docs/test.md/pep8/test-pep8-forms.png) | ✅
|blog/urls.py | All clear, no errors found |![Result](/docs/test.md/pep8/test-pep8-urls.png)| ✅
|blog/admin.py | All clear, no errors found |![Result](/docs/test.md/pep8/test-pep8-admin.png)| ✅
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Accessibility

### **Wave**

[The WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) was used to assess the accessibility of the website. WAVE helps identify potential accessibility issues and provides guidance on how to improve the accessibility of web content.

During the evaluation, the following issues were identified:

- **Errors**: The website generated 4 errors, which was related to the footer `<a>` (anchor) tags. There was no `aria-label` or text describing them. This was, of course, added to fix the errors.

- **Contrast Warning**: Received a contrast warning for primary button, which was blue used by Bootstrap's class "btn-primary". This color was not good against my dark purple background. Solution was to increase the primary button's blue color to a lighter shade.

<center> 

![Wave image](/docs/test.md/test-accessibility.png) 

</center>

By using the WAVE tool, I gained valuable insights into the accessibility of my website. While I have chosen not to address certain errors at this time, I remain committed to creating an inclusive user experience and will continue to explore ways to improve accessibility in the future.

<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Performance
We conducted a comprehensive evaluation of [The Gamers Insight website](https://game-insight-1cff11f2b2d5.herokuapp.com/) using [Google Lighthouse in Google Chrome Developer Tools](https://developer.chrome.com/docs/lighthouse/). This evaluation was performed in Google Chrome browser's incognito mode to eliminate all potential impacts from other addons and cached files.

Known Errors Impacting `index.html` and `post_detail.html` Pages the most, but even edit/delete post pages. We are using Cloudinary as an image and storage server for users to upload their images. The following errors were identified during Lighthouse validation, and they currently cannot be changed. These errors have had an impact on the overall performance of these pages:

- Serving images in next-gen formats
- Properly sizing images
- Efficiently encoding images
- Eliminating render-blocking resources

The performance scores were assessed for both desktop and mobile devices. Below are the summarized results:

### Desktop Performance
- Average performance score: 98/100
- The majority of pages received scores above 90/100, indicating excellent performance.

| **Tested** | **Performance Score** | **View Result** | **Pass** |
--- | --- | --- | :---:
|landing_page.html| 93 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-landing_page.png)</details> | ✅
|about.html| 92 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-about.png)</details> | ✅
|login.html| 100 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-login.png)</details> | ✅
|signup.html | 100 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-signup.png)</details> | ✅
|index.html| 93 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-index.png)</details> | ✅
|post_detail.html| 92 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-post_details.png)</details> | ✅
|contactus.html| 92 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-contactus.png)</details> | ✅
|contactus_success.html| 100 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-contact-success.png)</details>| ✅
|profile.html| 100 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-profile.png)</details> | ✅
|my_articles.html| 99 / 100| <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-myarticles.png)</details> | ✅
|post_create.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-create_post.png)</details> | ✅
|logout.html| 100 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-logout.png)</details> | ✅
|post_delete.html| 100 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-post_delete.png)</details> | ✅
|post_update.html| 100 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-post_update.png)</details> | ✅
|profile_delete.html| 100 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-profile_delete.png)</details> | ✅
|profile_update.html| 100 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-profile_update.png)</details> | ✅
|password_change.html| 100 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-password_change.png)</details> | ✅

### Mobile Performance
- Average performance score: 92/100
- The pages showed slightly lower performance compared to desktop, but still maintained a satisfactory score.

| **Tested** | **Performance** | **View Result** | **Pass** |
--- | --- | --- | :---:
|landing_page.html| 92 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-landing_page.png)</details> | ✅
|about.html| 94 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-about.png)</details> | ✅
|login.html| 96 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-login.png)</details> | ✅
|signup.html | 96 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-signup.png)</details> | ✅
|index.html| 80 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-index.png)</details> | ✅
|post_detail.html| 83 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-post_details.png)</details> | ✅
|contactus.html| 96 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-contactus.png)</details> | ✅
|contactus_success.html| 96 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-contact-success.png)</details>| ✅
|profile.html| 96 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-profile.png)</details> | ✅
|my_articles.html| 86 / 100| <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-myacrticles.png)</details> | ✅
|post_create.html| 86 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-post_create.png)</details> | ✅
|logout.html| 96 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-logout.png)</details> | ✅
|post_delete.html| 95 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-post_delete.png)</details> | ✅
|post_update.html| 93 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-post_update.png)</details> | ✅
|profile_delete.html| 96 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-profile_delete.png)</details> | ✅
|profile_update.html| 95 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-profile_update.png)</details> | ✅
|password_change.html| 95 / 100 | <details><summary>Screenshot of result</summary>![Result](/docs/test.md/lighthouse/test-lighthouse-mobile-password_change.png)</details> | ✅


In terms of performance, the Gamers Insight website delivered strong results, ensuring a seamless user experience on both desktop and mobile platforms.

<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Performing tests on various devices
The website was tested on the following devices:

<ins>Mobile</ins>
1. Samsung s22 ultra 
2. Iphone X 
3. Samsung galaxy s22
4. Iphone 14 pro max

<ins>Desktop</ins>
1. Samsung galaxy book 360
2. HP elite book 830 g9
3. HP victus gaming desktop

<ins>Monitors</ins>
1. 49 inch Samsung CHG9 ultra wide
2. 27 inch Benq zowie XL2746S
3. 27 inch Dell ultrasharp U2723QE

In addition, the website was tested using Google Chrome Developer Tools Device Toggeling option for all available device options.

<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Browser compability
The website was tested on the following:

<ins>Browsers</ins>
1. Microsoft Edge
2. Google Chrome 	
3. Mozilla firefox 	
4. Safari

<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Manual Testing

### Testing user stories

&nbsp;

**First Time Visitors**

| First Time User Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| [Easily Navigate and Find Content](https://github.com/KimBergstroem/PP4/issues/1) | Implemented a big navbar with navigation links that clearly state their purpose. Included two prominent login and sign-up buttons. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-first-navbar.png)</details> |
| [Visually Appealing Homepage](https://github.com/KimBergstroem/PP4/issues/2) | Created a landing page featuring a small animation of a magic book image and an engaging call-to-action header. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-first-homep.png)</details> |
| [Search for Specific Games or Topics](https://github.com/KimBergstroem/PP4/issues/3) | Displayed category buttons on the homepage, enabling users to easily navigate content by category. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-first-category.png)</details> |
| [Create a Personalized Profile](https://github.com/KimBergstroem/PP4/issues/5) | Automatically redirected first-time users to their profile page upon login, where they have the option to update their profile to their liking. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-first-profileupdate.png)</details> |

**Returning Visitors**

| Returning User Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| [Read Detailed Game Reviews](https://github.com/KimBergstroem/PP4/issues/4) | Users can access detailed game reviews by clicking on the "Articles" menu. They can click on the info button or the article itself to view more details about the game blog post. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-returning-gamereviews.png)</details> |
| [Save Favorite Articles and Create Reading Lists](https://github.com/KimBergstroem/PP4/issues/6) | Although not fully implemented, users have a "My Articles" menu in their profile where they can view posts they've liked and created. In the future, this section will also include favorites. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-returning-like.png)</details> |
| [Receive Notifications](https://github.com/KimBergstroem/PP4/issues/7) | While not fully implemented yet, there are plans to introduce a notification system, similar to a newsletter, in the near future. | <details><summary>Screenshot of result</summary>![Result](#)</details> |
| [Leave Comments and Engage in Discussions](https://github.com/KimBergstroem/PP4/issues/8) | Users can engage in discussions by leaving comments on other blog articles. There are no limits on submissions, and users can interact with one another. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-returning-comments.png)</details> |
| [Submit Own Articles and Reviews](https://github.com/KimBergstroem/PP4/issues/9) | Users can create their own blog posts by accessing the "Create Post" menu on their profile. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-returning-createpost.png)</details> |
| [Edit or Delete Own Articles and Comments](https://github.com/KimBergstroem/PP4/issues/10) | On individual blog posts, users have the option to edit or delete the post. This option is available only to the user who created the post. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-returning-deletepost.png)</details> |
| [Earn Badges or Rewards](https://github.com/KimBergstroem/PP4/issues/11) | Currently, the only reward system in place is related to liked posts. This information can also be viewed in the "My Articles" section of a user's profile. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-returning-myarticles.png)</details> |
| [Create Personalized Gaming Profile](https://github.com/KimBergstroem/PP4/issues/16) | Users can customize their gaming profile by visiting their profile page and updating their information. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-returning-updateprofile.png)</details> |
| [Save Favorite Articles and Create Reading Lists](https://github.com/KimBergstroem/PP4/issues/17) | Users can like other posts or create posts, and all this information will be saved in the "My Articles" section, making it easily accessible. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-returning-likedarticles.png)</details> |


**Site Owner**

| Site Owner Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| [Full Control Over User Accounts](https://github.com/KimBergstroem/PP4/issues/12) | Site owners or admin users have access to an admin dashboard where they can have complete control over user accounts, including management and oversight. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-owner-useraccount.png)</details> |
| [Review and Edit User-Submitted Articles](https://github.com/KimBergstroem/PP4/issues/13) | Admins or site owners can effectively review and edit user-submitted articles through the admin dashboard, which provides a convenient list view for article management. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-owner-posts.png)</details> |
| [Manage and Categorize Articles](https://github.com/KimBergstroem/PP4/issues/14) | Site owners or admins can manage article categories by adding, deleting, and overseeing them in the admin dashboard. Any changes made here will be reflected in the web application's category structure. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-owner-manage-posts.png)</details> |
| [Track User Engagement and Analytics](https://github.com/KimBergstroem/PP4/issues/15) | Admins or site owners can monitor user engagement and analytics through the dashboard, providing insights into articles, comments, and overall user activity on the platform. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/test-userstories-owner-manage-users.png)</details> |



&nbsp;

### User Experience and improvements
I engaged in user testing involving individuals from the Slack group called "#peer-code-review" from Code Institute to collect feedback regarding their website experience. I requested them to complete the following tasks and share their feedback on their overall experience:

I also asked family members and friends. 

Total users attended to the testing: 8

| Test                   | Result  |
|------------------------|---------|
| Create an account      | **100%**|
| Update the profile     | **100%**|
| Add a blog post        | **100%**|
| Edit a post            | **100%**|
| Like a post            | **100%**|
| Unlike a post          | **100%**|
| Comment on a post      | **100%**|
| Delete comment         | **100%**|
| Delete a post          | **100%**|
| Test links             | **100%**|
| Delete account         | **100%**|

&nbsp;

**Feedback from testers**

Provided feedback and reported any issues or improvements they encountered during the testing process. Below is the feedback/issues reported.

| **Feature**          | **Feedback**                                                                                                                                                                                                                                      | **Solution**                                                                                                                                                                              | **Result**                            | **Fixed** |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|:--------:|
| Navbar               | Social links are not opened in a new TAB                                                                                                                                                                                                           | Added 'target="_blank"' to the `a` tags.                                                                                                                                                  | Social links now open in a new tab. | ✅  |
| Max Length           | Max length should be reduced in different fields (Check all inputs forms models) Content Excerpt                                                                                                                                               | Added 'max_length=' both in `form.py` and `models.py` for client and server-side validation.                                                                                                                                                           | Max length reduced for various fields to improve validation. | ✅  |
| Post Details Icon    | Post details: Thumbs up is a heart instead, maybe confusing. Stick with the same icon.                                                                                                                                                          | Changed to a thumbs-up icon to match the blog post page.                                                                                                                                 | Post details now use a consistent thumbs-up icon.        | ✅  |
| Author Link          | In `index.html` (blog main page), the Author name is not clickable, and the like comment icons look like they should be clickable. Present them in a different way maybe?                                                                      | I removed the clickable link to the user's author profile for the post. I kept the icon display as it is for design purposes, which is a common way to display 'liked' posts and the number of comments. Additionally, I added a tooltip mouse hover card that explains to users that they need to visit the post detail page if they want to like the post.                                                                                        | Author name is no longer clickable; icons remain the same. | ✅  |
| Comment Max Length   | Post Details - Comment input has no max length, fix max length.                                                                                                                                                                                  | Added `max_length=300` in my Comment(model) for the comment field in post_details. Also added custom CSS media queries to present the comment in different screens so that no overflow breaks the comment field. | Comment input now has a max length, and it's presented properly on different screens.                     | ✅  |
| Profile picture | Users who update their profile picture should also see it displayed in the profile menu icon at the top right corner of the website. | Initially, attempted to display the user's profile picture instead of the current icon, but I found that it didn't look as good as the existing settings. Therefore, I decided to keep the profile icon as it is. | The profile icon remains unchanged for a better user experience. | ✅ |
| Delete / Edit | In the post_detail page, the "Edit" and "Delete" post and comment text are not displayed very well. I would prefer icons for better visualization. | Added more spacing between the words and also included icons for "Delete" and "Edit" for improved visualization. | "Edit" and "Delete" now have both text and icons. | ✅ |  
| Responsive           | Responsive needs to be fixed - Profile picture (nav menu collapse), Category buttons, Navbar in the smallest screens, it pops out of GAMERS INSIGHT and not in the same row. | Added custom styles with media queries to quickly fix responsiveness issues. Used small Bootstrap classes in some cases.                                                                                                                           | Responsive design improvements implemented.                | ✅  |

### Full Testing



**`Navbar unauthorized user`** 

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |



**`Navbar authorized user`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Profile drop down menu`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Index page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`About page unauthorized user`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`About page authorized user`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Sign up page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Log in page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Contact us page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Update profile page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Delete profile page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Post Detail page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Update post page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Delete post page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Change password page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`403,404,405, 500 Page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Summary
Overall, the Gamers Insight's website performed well in in all testings. The issues identified were acknowledged, and some were not addressed at the time due to design choices. 

<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>
