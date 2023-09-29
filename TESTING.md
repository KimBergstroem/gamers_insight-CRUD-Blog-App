# Gamers Insight Testing 

![Gamers Insight viewed in different screens](/docs/test.md/test.md-hero-image.png)

[View Live site here](https://kimbergstroem.github.io/PP4/)

[View Live site responsive here]()

---

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

---

**Throughout the game development process, I relied on Google Developer Tools to experiment with different elements and phases of the game. Additionally, I leveraged the console section in Chrome Dev Tools to test JavaScript code and address any problems or glitches that occurred in the code.**

---

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


## Browser compability
The website was tested on the following:

<ins>Browsers</ins>
1. Microsoft Edge
2. Google Chrome 	
3. Mozilla firefox 	
4. Safari


## Manual Testing

### Testing user stories

&nbsp;

**First Time Visitors**

| First Time User Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| [Easily Navigate and Find Content ](https://github.com/KimBergstroem/PP4/issues/1)  | Describe how first-time visitors can easily navigate and find content on your website. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Visually Appealing Homepage ](https://github.com/KimBergstroem/PP4/issues/2)  | Explain how you have designed the homepage to be visually appealing for first-time visitors. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Search for Specific Games or Topics ](https://github.com/KimBergstroem/PP4/issues/3)  | Describe the search functionality that allows first-time visitors to find specific games or topics. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Create a Personalized Profile ](https://github.com/KimBergstroem/PP4/issues/5)  | Explain how first-time visitors can create a personalized profile if they choose to do so. | <details><summary>Screenshot of result</summary>![Result]()</details> |

**Returning Visitors**

| Returning User Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| [Read Detailed Game Reviews ](https://github.com/KimBergstroem/PP4/issues/4)  | Describe how returning visitors can access and read detailed game reviews. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Save Favorite Articles and Create Reading Lists ](https://github.com/KimBergstroem/PP4/issues/6)  | Explain how returning visitors can save favorite articles and create reading lists. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Receive Notifications ](https://github.com/KimBergstroem/PP4/issues/7)  | Describe any notification features for returning visitors and how they work. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Leave Comments and Engage in Discussions ](https://github.com/KimBergstroem/PP4/issues/8)  | Explain how returning visitors can leave comments and engage in discussions. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Submit Own Articles and Reviews ](https://github.com/KimBergstroem/PP4/issues/9)  | Describe how returning visitors can submit their own articles and reviews. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Edit or Delete Own Articles and Comments ](https://github.com/KimBergstroem/PP4/issues/10)  | Explain how returning visitors can edit or delete their own articles and comments. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Earn Badges or Rewards ](https://github.com/KimBergstroem/PP4/issues/11)  | If applicable, describe any badge or reward systems for returning visitors. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Create Personalized Gaming Profile ](https://github.com/KimBergstroem/PP4/issues/16) | Explain how returning visitors can create personalized gaming profiles. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Save Favorite Articles and Create Reading List ](https://github.com/KimBergstroem/PP4/issues/17)  | Describe any additional features related to saving articles and creating reading lists. | <details><summary>Screenshot of result</summary>![Result]()</details> |

**Site Owner**

| Site Owner Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| [Full Control Over User Accounts ](https://github.com/KimBergstroem/PP4/issues/12)  | Explain how site owners have full control over user accounts and what actions they can take. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Review and Edit User-Submitted Articles ](https://github.com/KimBergstroem/PP4/issues/13)  | Describe the process by which site owners can review and edit user-submitted articles. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Manage and Categorize Articles ](https://github.com/KimBergstroem/PP4/issues/14)  | Explain how site owners can manage and categorize articles, if applicable. | <details><summary>Screenshot of result</summary>![Result]()</details> |
| [Track User Engagement and Analytics ](https://github.com/KimBergstroem/PP4/issues/15)  | Describe any tools or features site owners have for tracking user engagement and analytics. | <details><summary>Screenshot of result</summary>![Result]()</details> |


&nbsp;

### User Experience and improvements
I engaged in user testing involving individuals from the Slack group called "#peer-code-review" from Code Institute to collect feedback regarding their website experience. I requested them to complete the following tasks and share their feedback on their overall experience:

I also asked family members and friends. 

Total users attended to the testing: 10

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


**Feedback from testers**

&nbsp;&nbsp;

### Full Testing

&nbsp;

**`Home Page Section`** 

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |



**`Game Page Section`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Show score Section`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Highscore Section`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`Rules Section`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

**`404 Page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |
| Coming | Coming | Coming | ✅ |

