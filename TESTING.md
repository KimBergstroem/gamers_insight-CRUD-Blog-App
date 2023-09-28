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

## **Code Validation**

### HTML Validation

### **W3C Validator** 

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

## **Accessibility**

### **Wave**

[The WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) was used to assess the accessibility of the website. WAVE helps identify potential accessibility issues and provides guidance on how to improve the accessibility of web content.

During the evaluation, the following issues were identified:

- **Errors**: The website generated 4 errors, which was related to the footer `<a>` (anchor) tags. There was no `aria-label` or text describing them.

- **Contrast Warning**: Received a contrast warning for primary button, which was blue used by Bootstrap's class "btn-primary". This color was not good against my dark purple background. Solution was to increase the primary button's blue color to a lighter shade.

<center> 

![Wave image](/docs/test.md/test-accessibility.png) 

</center>

By using the WAVE tool, I gained valuable insights into the accessibility of my website. While I have chosen not to address certain errors at this time, I remain committed to creating an inclusive user experience and will continue to explore ways to improve accessibility in the future.


## **Performance**

### **Lighthouse** 

Desktop

Mobile

---

## **Manual Testing**

### **Testing User Stories**


**`First Time Visitors`**

| First Time User Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| Coming | Coming | <details><summary>Screenshot of result</summary>![Result]()</details> |
| Coming | Coming | <details><summary>Screenshot of result</summary>![Result]()</details> |
| Coming | Coming | <details><summary>Screenshot of result</summary>![Result]()</details> |
| Coming | Coming | <details><summary>Screenshot of result</summary>![Result]()</details> |



**`Returning Visitors`**

| Returning User Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| Coming | Coming | <details><summary>Screenshot of result</summary>![Result]()</details> |
| Coming | Coming | <details><summary>Screenshot of result</summary>![Result]()</details> |
| Coming | Coming | <details><summary>Screenshot of result</summary>![Result]()</details> |
| Coming | Coming | <details><summary>Screenshot of result</summary>![Result]()</details> |

&nbsp;

---
### **Full Testing**

Full Testing was performed on these devices and browsers for each section of game. 
I have utilized the Google Chrome Developer Tools and the Inspector tool to meticulously examine every page, ensuring their responsiveness across various screen sizes and devices.

**Devices**

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


<ins>Browsers</ins>
1. Microsoft Edge
2. Google Chrome 	
3. Mozilla firefox 	
4. Safari


&nbsp;

I also asked family and friends to test my game on their devices no issues were reported.

The scores below are the average results obtained from three users who attempted the following.
 
|Test|Result  |
|--|--|
|Coming |**100%**|
|Coming |**100%**|
|Coming |**100%**|
|Coming |**100%**|

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

