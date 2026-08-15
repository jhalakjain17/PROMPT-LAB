
def render_web():
    import streamlit as st
    from config import MODEL_TEMPERATURE,MAX_TOKEN_ALLOWED
    from prompts.prompt_builder import PromptBuilder
    from services.groq_service import GorqService

    OPTIONS = {
        "zero shot" : "zero_shot",
        "one shot " : "one_shot"
    }

    # Page title
    st.set_page_config(
        page_title= "Prompt Lab",
        page_icon="😎",
        layout='wide'
    )

    # Heading and Paragraph
    st.title("Prompt Engineering Lab")
    st.write("Learn Prompt Engineering By Doing")

    # Dropdown
    prompt_type = st.selectbox(
        "select the prompt Technique",
        OPTIONS.keys()
    )
    
    # Text Box
    user_prompt = st.text_area("Enter the Prompt",height=150)
    tokens= st.slider("Maximum Tokens:",min_value=100,max_value=2000,value=int(MAX_TOKEN_ALLOWED))
    temperature = st.slider("Temperature Range:",min_value=float(MODEL_TEMPERATURE),max_value=float(1))

    # Button
    if st.button("Generate Prompt"):
        if user_prompt.strip() == "":
            st.warning("Please Enter the Prompt")
        else:
            # st.success("Prompt Given Success")
            final_prompt=PromptBuilder.build(
                OPTIONS.get(prompt_type),user_prompt
            )

            groq=GorqService()
            response=groq.generate_response(final_prompt,temperature,tokens)

            
            st.subheader("Generate Prompt")
            st.code(final_prompt)
            st.subheader("Groq Response")
            st.code(response)

            # streamlite run web.py

if __name__ == "__main__":
    render_web()        