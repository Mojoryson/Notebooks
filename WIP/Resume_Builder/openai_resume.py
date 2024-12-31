# %% [markdown]
# # Resume Optimizer using AI

# %%
# Install Libs
!pip install openai markdown weasyprint

# %% [markdown]
# **Import the Libraries**

# %%
from IPython.display import display, Markdown
import os
import openai
from markdown import markdown
from weasyprint import HTML

# Connect to OpenAI
openai.api_key = os.getenv("OPENAI_KEY")

# %% [markdown]
# ### Import Resume and Job Description

# %%
# Open and Read the resume.md 
with open("resume/morrison_resume.md", "r", encoding="utf-8") as file:
    resume_string = file.read()

display(Markdown(resume_string))

# %%
# Prompt user for job data
jd_string = "" 
while not jd_string:  # Loop until we get some input
    print("To help me analyze this job description for you, please paste the full text below:")
    jd_string = input()
    if not jd_string:
        print("Oops! Looks like you didn't paste anything. Please try again.")
        
print(jd_string)

# %% [markdown]
# Build the Prompt Template

# %%
prompt_template = lambda resume_string, jd_string : f"""
You are a professional resume optimization expert specializing in tailoring resumes to specific job descriptions. Your goal is to optimize my resume and provide actionable suggestions for improvement to align with the target role.

### Guidelines:
1. **Relevance**:  
   - Prioritize experiences, skills, and achievements **most relevant to the job description**.  
   - Remove or de-emphasize irrelevant details to ensure a **concise** and **targeted** resume.
   - Limit work experience section to 4-5 most relevant roles
   - Limit bullet points under each role to 3-4 most relevant impacts

2. **Action-Driven Results**:  
   - Use **strong action verbs** and **quantifiable results** (e.g., percentages, revenue, efficiency improvements) to highlight impact.  

3. **Keyword Optimization**:  
   - Integrate **keywords** and phrases from the job description naturally to optimize for ATS (Applicant Tracking Systems).  

4. **Additional Suggestions** *(If Gaps Exist)*:  
   - If the resume does not fully align with the job description, suggest:  
     1. **Additional technical or soft skills** that I could add to make my profile stronger.  
     2. **Certifications or courses** I could pursue to bridge the gap.  
     3. **Project ideas or experiences** that would better align with the role.  

5. **Formatting**:  
   - Output the tailored resume in **clean Markdown format**.  
   - Include an **"Additional Suggestions"** section at the end with actionable improvement recommendations.  
   - Aim for a resume length of around 750-1000 words.
   - Tailor the tone and style to match the target company and industry.

---

### Input:
- **My resume**:  
{resume_string}

- **The job description**:  
{jd_string}

---

### Output:  
 **Tailored Resume**:  
   - A resume in **Markdown format** that emphasizes relevant experience, skills, and achievements.  
   - Incorporates job description **keywords** to optimize for ATS.  
   - Uses strong language and is no longer than **two pages**.

 **Contact Information:**  <-- Separate section for contact info
    - Include all provided contact details (email, phone, LinkedIn, GitHub).

 **Certifications:**  <-- Separate section for certifications at the bottom
    - Include all provided certifications with links.

## Addtional Suggestions:  <-- Separate section for suggestions
    - Include any additional suggestions for improvement based on the job description.
 **Additional Suggestions** *(if applicable)*:
   - Determine if the resume and experience is a **FIT** and a good candidate for this specific role.
   - List **skills** that could strengthen alignment with the role.  
   - Recommend **certifications or courses** to pursue.  
   - Suggest **specific projects or experiences** to develop.
   - Do not include "```markdown\n" or "```" in the response.

 **Evaluate as if you are the hiring manager the resume and experience against the job description to determine if the candidate is:
   - **FIT**: Fully meets or exceeds requirements.
   - **CLOSE**: Meets most requirements with minor gaps.
   - **STRETCH**: Has significant gaps but potential to grow into the role.

"""

# %%
# List all available models
models = openai.Model.list()

# Print the names of the models
for model in models['data']:
    print(model['id'])

# %%
prompt = prompt_template(resume_string, jd_string)

# %%
# Make API call
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Expert resume writer"},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
)

# Extract the response content
generated_text = response.choices[0].message.content # FIX VARIABLE NAME

# %%
print(response)

# %%
print(generated_text) # fix this

# %% [markdown]
# ### Display the results

# %%
resume_list = generated_text.split("## Additional Suggestions")

# %% [markdown]
# ## NEED COMMENTS

# %%
display(Markdown(resume_list[0]))

# %% [markdown]
# ### Save File to PDF & HTML

# %%
# Save to PDF
output_resume_pdf = "resume/openai_resume_new.pdf"

# Convert Markdown to HTML
html_output = markdown(resume_list[0])
print(html_output)

# %%
from markdown import markdown

def markdown_to_html_with_css(markdown_text, css_file="styles.css", google_font="Roboto"):
  """
  Converts markdown text to HTML, applies an external CSS file, and adds a Google Font.

  Args:
    markdown_text: The markdown text to convert.
    css_file: The path to the CSS file.
    google_font: The name of the Google Font to use.

  Returns:
    The HTML output as a string.
  """

  html_output = markdown(markdown_text)

  # Construct the HTML with the linked CSS file and Google Font
  html_with_css = f"""
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="UTF-8">
    <title>Resume</title>
    <link rel="stylesheet" href="{css_file}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family={google_font}&display=swap" rel="stylesheet">
  </head>
  <body>
    {html_output}
  </body>
  </html>
  """

  return html_with_css

# Example usage with resume_list and a Google Font:
html_output = markdown_to_html_with_css(resume_list[0], google_font="Open+Sans")

# Now you can save html_output to a file or use it further
print(html_output)

# Specify the filename
filename = "openai_resume.html"

# Write the HTML to the file
with open(filename, "w") as f:
  f.write(html_output)

print(f"HTML file saved as {filename}")

# %%
print(html_output)

# %%
# Save to PDF
output_resume_pdf = "resume/openai_resume_new.pdf"

# Convert HTML to PDF and save
HTML(string=html_output).write_pdf(output_resume_pdf, stylesheets=['styles.css'])

# %%
print(resume_list[0])

# %%
# save as markdown
output_file = "resume/openai_resume_new.md"

with open(output_file, "w", encoding="utf-8") as file:
    file.write(resume_list[0])

# %%
display(Markdown(resume_list[1]))

# %%



