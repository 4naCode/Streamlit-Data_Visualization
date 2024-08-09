import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#set page configuration
st.set_page_config(page_title="Visualization Data", layout="centered", page_icon="")
#title
st.title("Visualization Data")

#grettting
working_dif = os.path.dirname(os.path.abspath(__file__))

folder_path = f"{working_dif}/data"
 # Define the folder path
#folder_path = f"D:\\Dashboard\\apps\\data"
# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Upload file widget
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Save the uploaded file to the specified folder
    file_path = os.path.join(folder_path, uploaded_file.name)
    
    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
#list the files
files_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

#dropsown for all
selected_file = st.selectbox("select a file", files_list, index=None)

if selected_file:
    file_path = os.path.join(folder_path, selected_file)
    
    df=pd.read_csv(file_path)

    col1, col2 = st.columns(2)

    columns = df.columns.tolist()

    with col1:
        st.write("")
        st.write(df.head())

    with col2:
        # Allow the user to select columns for plotting
        x_axis = st.selectbox('Select the X-axis', options=columns+["None"])
        y_axis = st.selectbox('Select the Y-axis', options=columns+["None"])

        plot_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', 'Distribution Plot', 'Count Plot']
        # Allow the user to select the type of plot
        plot_type = st.selectbox('Select the type of plot', options=plot_list)

    # Generate the plot based on user selection
    if st.button('Generate Plot'):

        fig, ax = plt.subplots(figsize=(6, 4))

        if plot_type == 'Line Plot':
            sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
        elif plot_type == 'Bar Chart':
            sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
        elif plot_type == 'Scatter Plot':
            sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
        elif plot_type == 'Distribution Plot':
            sns.histplot(df[x_axis], kde=True, ax=ax)
            y_axis='Density'
        elif plot_type == 'Count Plot':
            sns.countplot(x=df[x_axis], ax=ax)
            y_axis = 'Count'

        # Adjust label sizes
        ax.tick_params(axis='x', labelsize=10)  # Adjust x-axis label size
        ax.tick_params(axis='y', labelsize=10)  # Adjust y-axis label size

        # Adjust title and axis labels with a smaller font size
        plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=12)
        plt.xlabel(x_axis, fontsize=10)
        plt.ylabel(y_axis, fontsize=10)

        # Show the results
        st.pyplot(fig)
