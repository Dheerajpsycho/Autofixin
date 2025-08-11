import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Page Setup ---
st.set_page_config(page_title="AutoFixin - Car Service & Repair", page_icon="🚗", layout="wide")

st.markdown("""
    <style>
        .main {
            background-color: #f2f2f2;
        }
        .title-style {
            font-size: 60px;
            font-weight: bold;
            color: #003366;
        }
        .subheader-style {
            font-size: 24px;
            color: #444;
        }
    </style>
""", unsafe_allow_html=True)


# --- Logo and Title ---
# Display company logo (first uploaded image)
st.image("Logo.png", width=200)  

# Display main brand image (second uploaded image instead of car icon)
st.image("Name.png", width=300)  

# Title and tagline
#st.markdown("<div class='title-style'>AutoFixin</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader-style'>Your trusted partner for car repair, maintenance, and detailing.</div>", unsafe_allow_html=True)


# --- Services Section ---
st.header("🌟 Our Services")
st.markdown("""
- **General Car Servicing**
- **All German car repair expert**
- **Engine Diagnostics**
- **Brake and Clutch Repairs**
- **AC and Electrical Works**
- **Car Washing & Detailing**
- **Doorstep Pickup and Drop Facility**
""")

# --- Booking Section ---
st.header("📅 Book a Service Appointment")
with st.form("booking_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Customer Name")
        phone = st.text_input("Contact Number")
        #address = st.text_input("Address")
        vehicle_model = st.text_input("Vehicle Model")
        service_type = st.selectbox("Service Type", ["General Servicing", "Engine Diagnostics", "Auto Transmission Repair", "Car Wash", "Other"])

    with col2:
        repair_summary = st.text_area("Repair Summary")
        appointment_date = st.date_input("Preferred Date", min_value=date.today())
        pickup_required = st.checkbox("Need Pickup & Drop?")

    submitted = st.form_submit_button("Book Now")

    if submitted:
        st.success(f"Thank you, {name}! Your {service_type} appointment for {vehicle_model} on {appointment_date} has been booked.")
        if pickup_required:
            st.info("Our team will contact you shortly to arrange pickup.")

        # --- Send Email ---
        sender_email = "dheeraj04k09@gmail.com"
        sender_password = "tlge tbzl euwu nmsh"
        receiver_email = "autofixinautomobiles@gmail.com"

        subject = f"New Service Appointment - {name}"
        body = f"""
Customer Name: {name}
Phone: {phone}
Vehicle Model: {vehicle_model}
Service Type: {service_type}
Appointment Date: {appointment_date}
Pickup Required: {'Yes' if pickup_required else 'No'}
Repair Summary: {repair_summary}
"""

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender_email, sender_password)
                server.send_message(msg)
                st.success("Booking email sent to AutoFixin inbox!")
        except Exception as e:
            st.error(f"Failed to send email: {e}")

# --- Terms and Conditions ---
st.header("📄 Terms and Conditions")
st.markdown("""
- Subject to our home jurisdiction.  
- Our responsibilities cease as soon as goods/vehicle/services leave our premises.  
- Parking charges apply before/after service at ₹200/day.  
- Routine maintenance and issue check in progress as per customer concerns.  
- Thank you for your confidence.
""")

# --- Contact Section ---
st.header("📞 Contact Us")
st.markdown("""
**Phone:** +91-9340681809, +91-8602432586 


**Email:** autofixinautomobiles@gmail.com  


**Address:** Shop no.5, Khasra no. 132, near business plaza, near Ci Square, akbarpur, Kolar Rd, Bhopal, Madhya Pradesh 462042.

Follow us on [Instagram](https://www.instagram.com/autofixin_automobiles?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==) | [Facebook](https://facebook.com)
""")



