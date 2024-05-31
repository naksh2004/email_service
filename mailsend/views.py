from django.core.mail import EmailMessage
from selenium import webdriver
from django.http import HttpResponse
from selenium.webdriver.common.by import By
import time
def send_email():
    # Open the browser
    driver = webdriver.Chrome() 
    # Open the Google Form
    driver.get("https://forms.gle/WT68aV5UnPajeoSc8")
    time.sleep(2)  # Wait for the page to load

    # Fill out the form fields
    full_name = driver.find_element(By.XPATH, "//*[@aria-describedby='i2 i3']")
    full_name.send_keys('Nakshatra Bansal')

    contact_number = driver.find_element(By.XPATH, "//*[@aria-describedby='i6 i7']")
    contact_number.send_keys('7742832920')

    email = driver.find_element(By.XPATH, "//*[@aria-describedby='i10 i11']")
    email.send_keys("naksh2904@gmail.com")

    address = driver.find_element(By.XPATH, "//*[@aria-describedby='i14 i15']")
    address.send_keys("23, Mayur Van Colony,sector-4 , udaipur , Rajasthan")

    pin_code = driver.find_element(By.XPATH, "//*[@aria-describedby='i18 i19']")
    pin_code.send_keys("313002")

    dob = driver.find_element(By.XPATH, "//*[@aria-labelledby='i25']")
   # dob.click()
    dob.send_keys("29042002")  

    # Gender selection
    gender = driver.find_element(By.XPATH, "//*[@aria-describedby='i27 i28']")
    gender.send_keys("Male")

    # Captcha input
    captcha_code = driver.find_element(By.XPATH, "//*[@aria-describedby='i31 i32']")
    captcha_code.send_keys("GNFPYC")

    # Submit the form
    submit_button = driver.find_element(By.CLASS_NAME, "lRwqcd")
    #submit_button.click()

    # Wait for the confirmation page to load
    time.sleep(5)

    # Take a screenshot of the confirmation page
    driver.save_screenshot("confirmation_page.png")

    # Close the browser
    driver.quit()
    email_subject = "Screenshot from Selenium WebDriver"
    email_body = "Please find the screenshot attached."
    from_email = "naksh2904@gmail.com"
    to_email = ["bansalyash179@gmail.com"]
    
    email = EmailMessage(email_subject, email_body, from_email, to_email)
    
    # Attach screenshot to the email
    email.attach_file('C:/Users/Dell/send_email/confirmation_page.png')

    # Send email
    email.send()

def my_view(request):
    # Your view logic here
    # Call the send_email function when needed
    send_email()
    return HttpResponse("Form submitted and email sent!")
