import re
from io import BytesIO

import fitz
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sahayak AI", page_icon="📄", layout="wide")


def extract_pdf_text(file_bytes: bytes) -> str:
    """Extract selectable text from a PDF. OCR can be added for scanned PDFs."""
    document = fitz.open(stream=file_bytes, filetype="pdf")
    return "\n".join(page.get_text() for page in document)


def find_amounts(text: str) -> list[str]:
    return list(dict.fromkeys(re.findall(r"(?:₹|Rs\.?|INR)\s?[\d,]+(?:\.\d{1,2})?", text, re.I)))[:4]


def find_dates(text: str) -> list[str]:
    matches = re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text)
    return list(dict.fromkeys(matches))[:4]


def demo_summary(text: str) -> tuple[str, list[str]]:
    """Demo fallback until a Qualcomm AI Hub local model is connected."""
    compact = " ".join(text.split())
    if not compact:
        return (
            "इस स्कैन किए गए दस्तावेज़ में चुनने योग्य टेक्स्ट नहीं मिला। OCR और स्थानीय vision-language मॉडल जोड़ने पर Sahayak AI इसे पढ़ सकेगा।",
            ["स्पष्ट फोटो या टेक्स्ट वाला PDF अपलोड करें", "OCR मॉडल से दस्तावेज़ पढ़ें"],
        )
    actions = ["दस्तावेज़ में बताई गई जरूरी जानकारी को ध्यान से जांचें"]
    if dates := find_dates(compact):
        actions.append(f"इन तारीखों को नोट करें: {', '.join(dates)}")
    if amounts := find_amounts(compact):
        actions.append(f"इन रकमों को सत्यापित करें: {', '.join(amounts)}")
    actions.append("यदि कोई भुगतान, आवेदन या जवाब जरूरी हो तो समय पर पूरा करें")
    return f"मुख्य टेक्स्ट: {compact[:420]}", actions


st.title("Sahayak AI")
st.caption("Private Hindi document guidance designed for Snapdragon-powered HP PCs")
st.write("Upload a document to receive a simple Hindi explanation, important dates and amounts, and an action checklist.")

uploaded_file = st.file_uploader("Upload a PDF or document image", type=["pdf", "png", "jpg", "jpeg"])
if uploaded_file:
    file_bytes = uploaded_file.getvalue()
    st.success(f"Document uploaded: {uploaded_file.name}")
    if uploaded_file.type == "application/pdf":
        try:
            extracted_text = extract_pdf_text(file_bytes)
            st.subheader("Document preview")
            st.text_area("Extracted text", extracted_text[:3000], height=180)
        except Exception as error:
            st.error(f"The PDF could not be read: {error}")
            extracted_text = ""
    else:
        st.image(Image.open(BytesIO(file_bytes)), caption="Uploaded document", width=520)
        extracted_text = ""
        st.warning("Image OCR will be enabled with the local Qualcomm model integration.")

    summary, actions = demo_summary(extracted_text)
    left, right = st.columns([1.2, 1])
    with left:
        st.subheader("सरल हिंदी में सारांश")
        st.write(summary)
    with right:
        st.subheader("आपको क्या करना है")
        for action in actions:
            st.write(f"- {action}")

    question = st.text_input("दस्तावेज़ के बारे में सवाल पूछें", placeholder="मुझे क्या करना है?")
    if question:
        st.success("Local Hindi model integration के बाद Sahayak AI इस सवाल का निजी, on-device उत्तर देगा।")
    st.info("Integration point: connect Qualcomm AI Hub vision-language and Hindi LLM models through GenieX or Qualcomm AI Runtime, plus local Whisper for voice input.")
else:
    st.info("Start by uploading a PDF, JPG, or PNG document.")

st.divider()
st.caption("Prototype architecture: local OCR + vision-language model + Hindi LLM + Whisper speech recognition")
