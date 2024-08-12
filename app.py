import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Center-align the title using Markdown
st.markdown("<h1 style='text-align: center;'>Data Analyst</h1>", unsafe_allow_html=True)

# Set the folder path where files will be saved
#folder_path = "path_to_save_files"
#youtube_video_url = "https://www.youtube.com/watch?v=tl_1unb5Asc"  # Replace with your YouTube video URL
#st.markdown(f"""
#    <iframe width="300" height="200" src="{youtube_video_url.replace('watch?v=', 'embed/')}" frameborder="0" allowfullscreen></iframe>
#    """, unsafe_allow_html=True)

# Define the working directory and image file name
working_dir = os.path.dirname(os.path.abspath(__file__))
image_folder_path = os.path.join(working_dir, 'image')
image_filename = "Data Visualization.PNG"
image_path = os.path.join(image_folder_path, image_filename)

col1, col2 = st.columns([2, 1], gap="small")  # Adjust the ratio as needed

# Display the image in the first column
with col1:
    if os.path.exists(image_path):
        st.image(image_path, use_column_width=True, clamp=True)  # Adjust width as needed
    else:
        st.error("Image file not found")

# Display the video in the second column
with col2:
    youtube_video_url = "https://www.youtube.com/watch?v=PVoZ86J3tGQ"  # Replace with your YouTube video URL
    st.markdown(f"""
        <div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; max-width:100%; height:auto;">
            <iframe src="{youtube_video_url.replace('watch?v=', 'embed/')}" frameborder="0" allowfullscreen
                    style="position:absolute; top:0; left:0; width:100%; height:100%;">
            </iframe>
        </div>
        """, unsafe_allow_html=True)

# Create the folder for uploaded files if it doesn't exist
data_folder_path = os.path.join(working_dir, 'data')
if not os.path.exists(data_folder_path):
    os.makedirs(data_folder_path)

# Upload file widget
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Save the uploaded file to the specified folder
    file_path = os.path.join(data_folder_path, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())

# List the files in the folder
files_list = [f for f in os.listdir(data_folder_path) if f.endswith((".csv", ".xlsx"))]

# Dropdown for file selection
selected_file = st.selectbox("Select a file", files_list, index=None)

if selected_file:
    file_path = os.path.join(data_folder_path, selected_file)
    if selected_file.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif selected_file.endswith(".xlsx"):
        df = pd.read_excel(file_path)

    col1, col2 = st.columns(2)

    columns = df.columns.tolist()
    object_columns = df.select_dtypes(include=['object']).columns.tolist()

    # Filter numeric columns for Y-axis selection
    numeric = df.select_dtypes(include=['number']).columns.tolist()

    with col1:
        st.write("")
        st.write(df.head())

    with col2:
        # Allow the user to select columns for plotting
        x_axis = st.selectbox('Select the X-axis', options=object_columns + ["None"])
        y_axis = st.selectbox('Select the Y-axis', options=numeric + ["None"])

        plot_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', 'Distribution Plot', 'Count Plot', 'Statistik deskriptif']
        # Allow the user to select the type of plot
        plot_type = st.selectbox('Select the type of plot', options=plot_list)




    # Generate the plot based on user selection
    if st.button('Generate Plot'):
        

  #     st.markdown(f"<h4 style='text-align: center;'>Max {x_axis}: {max_value:.2f}</h4>", unsafe_allow_html=True)
        if plot_type == 'Statistik deskriptif':
            #if x_axis not in df.columns or (df[x_axis].dtype != 'object' and df[y_axis] not in df.columns):
             #   st.error("Plot yang dipilih tidak sesuai. Pilih tipe plot selain Statistik Deskriptif atau pilih kolom yang sesuai")
            #else:
                if x_axis == "None" and y_axis == "None":
                    st.error("Error: Jangan sampai kolom y axis kosong ")

                elif x_axis != "None" and y_axis != "None":
                    st.error("Error: Khusus Statistik deskription kolom x axis dapat dikosongkan / None ")

                elif x_axis == "None" and y_axis != "None":
                    if y_axis in df.columns:
                        total = df[y_axis].sum()
                        average = df[y_axis].mean()
                        median = df[y_axis].median()
                        mode = df[y_axis].mode()[0]
                        min_value = df[y_axis].min()
                        max_value = df[y_axis].max()
                        st.markdown(f"<h4 style='text-align: center;'>Total {y_axis}: {total}</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style='text-align: center;'>Average {y_axis}: {average:.2f}</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style='text-align: center;'>Median {y_axis}: {median:.2f}</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style='text-align: center;'>Mode {y_axis}: {mode}</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style='text-align: center;'>Min {y_axis}: {min_value:.2f}</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style='text-align: center;'>Max {y_axis}: {max_value:.2f}</h4>", unsafe_allow_html=True)
                    else:
                        st.error(f"Column {y_axis} not found in DataFrame.")
                        
                elif x_axis != "None" and y_axis == "None":
                    if x_axis in df.columns:
                            # Periksa jika tipe data kolom x_axis adalah objek
                        if pd.api.types.is_object_dtype(df[x_axis]):
                            st.error("Plot yang dipilih tidak sesuai. Pilih tipe plot selain Statistik Deskriptif atau isi x axis dengan None.")
                        else:
                            st.error("Untuk statistik deskriptif, x_axis harus 'None' dan y_axis harus kolom numerik.")
                
                    else:
                        total = df[x_axis].sum()
                        average = df[x_axis].mean()
                        median = df[x_axis].median()
                        mode = df[x_axis].mode()[0]
                        min_value = df[x_axis].min()
                        max_value = df[x_axis].max()
                        st.markdown(f"<h4 style='text-align: center;'>Total {x_axis}: {total}</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style='text-align: center;'>Average {x_axis}: {average:.2f}</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style='text-align: center;'>Median {x_axis}: {median:.2f}</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style='text-align: center;'>Mode {x_axis}: {mode}</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style='text-align: center;'>Min {x_axis}: {min_value:.2f}</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style='text-align: center;'>Max {x_axis}: {max_value:.2f}</h4>", unsafe_allow_html=True)
                    
        else:

        # Create a figure and axis with a black background
            fig, ax = plt.subplots(figsize=(6, 4))
            fig.patch.set_facecolor('black')
            ax.set_facecolor('black')
        # Sort data by y-axis for Bar Chart and Count Plot
            if plot_type == 'Bar Chart':
                
                if x_axis == None:
                    st.error('Isi kolom dengan benar!!!')
                else:
                    # Count occurrences of each x_axis value and sort them
                    try:
                        # Group by x_axis and sum the y_axis, then sort by y_axis
                        grouped_df = df.groupby(x_axis)[y_axis].sum().reset_index()
                        sorted_df = grouped_df.sort_values(by=y_axis, ascending=False)
                        sns.barplot(x=sorted_df[x_axis], y=sorted_df[y_axis], ax=ax)
                    except KeyError as e:
                        st.error(f"Error:Visualisasi tidak dapat di tampilkan, Isi column x_axis & y_axis dengan benar. ")
                
            elif plot_type == 'Count Plot':
                if x_axis == None:
                    st.error('Isi kolom dengan benar!!!')
                else:
                    # Count occurrences of each x_axis value and sort them
                    try:
                        sorted_df = df[x_axis].value_counts().sort_values(ascending=False)
                        sns.countplot(x=sorted_df.index, order=sorted_df.index, ax=ax)
                        y_axis = 'Count'
                    except KeyError as e:
                        st.error(f"Error:Visualisasi tidak dapat di tampilkan, Isi column x_axis & y_axis dengan benar. ")

            elif plot_type == 'Line Plot':
                
                if not x_axis:
                    st.error('Isi kolom x_axis dengan benar!!!')
                else:
                    try:
                        sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
                    except KeyError as e:
                        st.error(f"Error: Visualisasi tidak dapat ditampilkan, Isi kolom x_axis & y_axis dengan benar.")

            elif plot_type == 'Scatter Plot':
                if not x_axis:
                    st.error('Isi kolom x_axis dengan benar!!!')
                else:
                    try:
                        sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
                    except KeyError as e:
                        st.error(f"Error: Visualisasi tidak dapat ditampilkan, Isi kolom x_axis & y_axis dengan benar.")

                
            elif plot_type == 'Distribution Plot':
                if not x_axis:
                    st.error('Isi kolom x_axis dengan benar!!!')
                else:
                    try:
                        sns.histplot(df[x_axis], kde=True, ax=ax)
                        y_axis = 'Density'
                    except KeyError as e:
                        st.error(f"Error: Visualisasi tidak dapat ditampilkan, Isi kolom x_axis & y_axis dengan benar.")

            
                    
            # Adjust label sizes
            ax.tick_params(axis='x', labelsize=10, colors='white')  # Adjust x-axis label size
            ax.tick_params(axis='y', labelsize=10, colors='white')  # Adjust y-axis label size
            # Add a grid with dashed lines and some transparency
            ax.grid(True, linestyle='--', alpha=0.4)
            #jika kata melebih 5 angka maka ubah rotation
            # Determine the number of unique values on the x-axis
            # Check if x_axis is valid before determining unique values
            
            # Flag to determine if any x-axis label is longer than 5 characters
            #long_label = any(len(str(label)) > 2 for label in df[x_axis].unique())

            # Adjust rotation based on the number of unique x-axis values and label length
            #if num_unique_values > 2 or long_label:
            for label in ax.get_xticklabels():
                label.set_rotation(80)
                label.set_ha('right')
            #else:
           # for label in ax.get_xticklabels():
            #    label.set_rotation(0)  # No rotation
            #    label.set_ha('center')  # Center alignment for better readability

            
            # Adjust title and axis labels with a smaller font size
            plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=12, color='white')
            plt.xlabel(x_axis, fontsize=10, color='white')
            plt.ylabel(y_axis, fontsize=10, color='white')

            # Show the results
            st.pyplot(fig)