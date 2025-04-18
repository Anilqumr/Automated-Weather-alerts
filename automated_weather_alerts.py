import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to get weather data from Open-Meteo API
def get_weather_data(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to send email alerts
def send_email_alert(subject, body, to_email):
    sender_email = "anilqumr@gmail.com"
    sender_password = "buyw waxw dchn wvnx"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to check weather conditions and send alerts
def check_for_alerts_and_notify(weather_data, recipient_email):
    hourly_temperature = weather_data['hourly']['temperature_2m'][0]
    hourly_precipitation = weather_data['hourly']['precipitation'][0]

    if hourly_temperature > 15:  # Temperature threshold
        alert_subject = "Heat Alert"
        alert_body = f"High temperature detected: {hourly_temperature}°C"
        send_email_alert(alert_subject, alert_body, recipient_email)

    if hourly_precipitation > 10:  # Precipitation threshold
        alert_subject = "Rain Alert"
        alert_body = f"Heavy rainfall expected: {hourly_precipitation}mm"
        send_email_alert(alert_subject, alert_body, recipient_email)

# Main program
if __name__ == "__main__":
    # Coordinates for Hyderabad
    latitude = 17.3850
    longitude = 78.4867
    recipient_email = "engbxxr@gmail.com"  # Change to actual recipient email
    
    # Fetch weather data
    weather_data = get_weather_data(latitude, longitude)
    
    if weather_data:
        print("Weather data fetched successfully!")
        check_for_alerts_and_notify(weather_data, recipient_email)
    else:
        print("Failed to fetch weather data.")
