import requests
import streamlit as st
from datetime import date, datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(page_title="AutoFixin — Premium Car Care", page_icon="Logo.png", layout="wide")

# ---------- Styles ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
html, body, [class*="css"]  { font-family: 'Poppins', sans-serif; }
.main { background: linear-gradient(180deg, #fff, #f7f7fb 60%, #eef3ff); }
.block-container { padding-top: 3rem; padding-bottom: 3rem; }

.hero {
  padding: 4.5rem 2rem;
  border-radius: 32px;
  background: radial-gradient(1200px 600px at 10% -10%, #ffe1d6 0%, transparent 60%),
              radial-gradient(1200px 600px at 100% 0%, #d7e8ff 0%, transparent 60%),
              linear-gradient(135deg, #ffefe9, #e9f0ff);
  text-align: center;
  box-shadow: 0 30px 80px rgba(0,0,0,.08);
}
.hero h1 { font-size: 3.2rem; margin: 0; color: #101828; }
.hero p { font-size: 1.15rem; color: #475467; margin-top: .6rem; }

.badge { display: inline-block; background: #101828; color: #fff; padding: .35rem .75rem; border-radius: 999px; font-size: .85rem; }
.cta { display: inline-block; padding: .85rem 1.2rem; border-radius: 14px; text-decoration:none; margin: .5rem; }
.cta-primary { background:#e64a19; color: #fff; }
.cta-ghost { border:1px solid #d0d5dd; color:#101828; background:#fff; }

.card {
  border-radius: 24px;
  padding: 1.2rem;
  background: rgba(255,255,255,.85);
  border: 1px solid #eef2f7;
  box-shadow: 0 15px 40px rgba(16,24,40,.06);
}
.card h3 { margin-top: .4rem; }

.section-title { font-weight: 700; font-size: 1.8rem; margin: 2.2rem 0 1rem; }
.kpi { font-size: 2rem; font-weight: 700; }

.footer { text-align:center; color:#667085; padding: 2rem 0 1rem; }
.stButton>button { border-radius: 12px; padding: .7rem 1.2rem; font-weight:600; }
.stTextInput>div>div>input, .stTextArea textarea, .stSelectbox select, .stDateInput>div>div>input {
  border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- Top Bar ----------
c1, c2, c3 = st.columns([1,2,1])
with c1:
    st.image("Logo.png", width=72)
with c2:
    st.image("Name.png", use_container_width=True)
with c3:
    st.markdown("<div style='text-align:right;'><span class='badge'>Bhopal • Since 2020</span></div>", unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown("""
<div class="hero">
  <span class="badge">Premium Car Service • German Specialists</span>
  <h1>Drive with confidence. We handle the rest.</h1>
  <p>AutoFixin brings dealership-grade diagnostics, OEM-quality parts, and friendly pricing—under one roof.</p>
  <div>
    <a class="cta cta-primary" href="#book">Book a Service</a>
    <a class="cta cta-ghost" href="https://wa.me/919340681809" target="_blank">WhatsApp Us</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------- KPIs ----------
k1,k2,k3,k4 = st.columns(4)
k1.metric("Vehicles Serviced", "10,000+")
k2.metric("German Cars/Month", "100+")
k3.metric("Customer Rating", "4.9/5")
k4.metric("Pickup Coverage", "Across Bhopal")

# ---------- Services Grid ----------
st.markdown('<div class="section-title">Our Services</div>', unsafe_allow_html=True)
rows = [
    ("img/car_service.png", "General Service",
     "OEM-quality oils & filters • 40+ checkpoints • Fluids top-up & calibration"),
    ("img/audi_detailing.png", "German Car Care",
     "Audi, BMW, Mercedes, Porsche, Range Rover, Land Rover, Jaguar, Mustang & VW specialists with advanced scan tools"),
    ("img/auto_transmission.png", "Engine Diagnostics",
     "OBD scanning • Live data • Leak tests • Accurate root-cause fixes"),
    ("img/tramsmission.png", "Brake & Clutch",
     "Pads, discs, hydraulics • Clutch plate & pressure plate replacement"),
    ("img/lap.png", "AC & Electrical",
     "AC performance restore • Alternator/Starter • Battery • Wiring & fuses"),
    ("img/tow.png", "Pickup & Drop",
     "Insured door-step pickup & delivery by trained drivers"),
]
for i in range(0, len(rows), 3):
    c = st.columns(3)
    for col, item in zip(c, rows[i:i+3]):
        img, title, desc = item
        with col:
            st.image(img, use_container_width=True)
            st.markdown(f"<div class='card'><h3>{title}</h3><p>{desc}</p></div>", unsafe_allow_html=True)

# ---------- Why Choose Us ----------
st.markdown('<div class="section-title">Why choose AutoFixin?</div>', unsafe_allow_html=True)
c1,c2,c3 = st.columns(3)
with c1: st.markdown("<div class='card'><h3>Expert Technicians</h3><p>Brand-trained team with decade+ combined experience.</p></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='card'><h3>Transparent Pricing</h3><p>No surprises. Written estimates before work begins.</p></div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='card'><h3>Genuine Parts</h3><p>OEM or equivalent-grade components, always.</p></div>", unsafe_allow_html=True)

# ---------- Pricing Snapshot ----------
st.markdown('<div class="section-title">Popular Packages</div>', unsafe_allow_html=True)
pc1, pc2, pc3 = st.columns(3)
with pc1:
    st.markdown("<div class='card'><h3>Basic Service</h3><p>Engine oil + filter, 25-point check, wash.</p><h2 class='kpi'>₹2,999*</h2></div>", unsafe_allow_html=True)
with pc2:
    st.markdown("<div class='card'><h3>Premium Service</h3><p>Fully synthetic oil, all filters, 40-point check.</p><h2 class='kpi'>₹6,999*</h2></div>", unsafe_allow_html=True)
with pc3:
    st.markdown("<div class='card'><h3>German Diagnostic</h3><p>Advanced scan, road test, report.</p><h2 class='kpi'>₹1,800</h2></div>", unsafe_allow_html=True)
st.caption("*Prices vary by model. Call for exact quotes.")

# ---------- Gallery ----------
st.markdown('<div class="section-title">Workshop Gallery</div>', unsafe_allow_html=True)
st.image([f"img/german.png" for i in range(1)], use_container_width=True)

# ---------- Booking ----------
st.markdown('<div class="section-title" id="book">Book a Service Appointment</div>', unsafe_allow_html=True)
with st.form("booking_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Customer Name")
        phone = st.text_input("Contact Number")
        vehicle_model = st.text_input("Vehicle Model")
        service_type = st.selectbox("Service Type", ["General Servicing", "Engine Diagnostics", "Auto Transmission Repair", "Car Wash", "Other"])
    with col2:
        repair_summary = st.text_area("Describe the issue / service required")
        appointment_date = st.date_input("Preferred Date", min_value=date.today())
        pickup_required = st.checkbox("Need Pickup & Drop?")

    submitted = st.form_submit_button("Book Now")
    if submitted:
        # Optional email via st.secrets (safer). Configure in .streamlit/secrets.toml
        sent_email = False
        try:
            sender_email = st.secrets.get("SMTP_USER", "")
            sender_password = st.secrets.get("SMTP_PASS", "")
            receiver_email = st.secrets.get("BOOKING_INBOX", "autofixinautomobiles@gmail.com")
            if sender_email and sender_password:
                subject = f"New Service Appointment - {name}"
                body = f"""
Customer Name: {name}
Phone: {phone}
Vehicle Model: {vehicle_model}
Service Type: {service_type}
Appointment Date: {appointment_date}
Pickup Required: {'Yes' if pickup_required else 'No'}
Repair Summary: {repair_summary}
Timestamp: {datetime.now()}
"""
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                    server.login(sender_email, sender_password)
                    server.send_message(msg)
                sent_email = True
        except Exception as e:
            st.warning(f"Email not sent (configure st.secrets). Error: {e}")

        st.success(f"Thanks, {name}! Your {service_type} appointment for {vehicle_model} on {appointment_date} is recorded.")
        if pickup_required:
            st.info("Our team will contact you shortly to arrange pickup.")
        if sent_email:
            st.success("Booking email sent to AutoFixin inbox!")
        else:
            st.caption("Tip: set SMTP_USER, SMTP_PASS & BOOKING_INBOX in Streamlit secrets to enable email alerts.")

# ---------- Terms & Contact ----------
st.markdown('<div class="section-title">Terms & Conditions</div>', unsafe_allow_html=True)
st.markdown("""
- Parking charges before/after service: ₹200/day.  
- Responsibilities cease once the vehicle leaves our premises.  
- Maintenance performed per concerns noted by the customer.  
- All disputes subject to Bhopal jurisdiction.
""")

st.markdown('<div class="section-title">Contact Us</div>', unsafe_allow_html=True)
st.markdown("""
**Phone:** +91-9340681809, +91-8602432586  
**Email:** autofixinautomobiles@gmail.com  
**Address:** Shop no.5, Khasra no. 132, near Business Plaza, near CI Square, Akbarpur, Kolar Rd, Bhopal, MP 462042.  
""")

st.markdown("""
<div class="footer">© {} AutoFixin. All rights reserved.</div>
""".format(date.today().year), unsafe_allow_html=True)

# ---------- AI CHATBOT (Floating Button) ----------

# Initialize chatbot toggle
if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

# Custom CSS for floating button
st.markdown("""
    <style>
    .floating-btn {
        position: fixed;
        bottom: 25px;
        right: 25px;
        background-color: #e64a19;
        color: white;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        font-size: 28px;
        text-align: center;
        line-height: 60px;
        cursor: pointer;
        z-index: 9999;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }
    </style>
""", unsafe_allow_html=True)

# Floating button
if st.button("💬", key="chat_toggle"):
    st.session_state.chat_open = not st.session_state.chat_open

# Chatbot panel
if st.session_state.chat_open:
    st.markdown("### 💬 Chat with AutoFixin AI")
    st.caption("Ask anything about car care, German vehicles, or our services.")

    user_input = st.text_area("Your question:", placeholder="e.g. Why is my BMW making a ticking noise?")

    if st.button("Ask AI", key="ask_ai_btn"):
        if not user_input.strip():
            st.warning("Please type a question first 🚗")
        else:
            with st.spinner("Thinking... ⚙️"):
                try:
                    API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
                    headers = {"Authorization": f"Bearer " + st.secrets.get("HF_TOKEN", "")}

                    payload = {
                        "inputs": f"Customer question: {user_input}\nAnswer in simple and professional car-care language:"
                    }

                    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)

                    if response.status_code == 200:
                        ai_reply = response.json()[0]["generated_text"]
                        st.success("🤖 AutoFixin AI says:")
                        st.write(ai_reply)
                    else:
                        st.error("⚠️ AI model is busy or unavailable. Please try again later.")

                except Exception as e:
                    st.error(f"Error: {e}")
                    st.info("Tip: Add your HuggingFace API key in `.streamlit/secrets.toml` like this:\n\nHF_TOKEN='your_hf_api_key'")



