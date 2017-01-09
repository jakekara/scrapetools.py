import scrapetools as st
import os

out_dir = "output"
# Create output directory
def make_directories():
    st.makedir(out_dir)
            
def get_seec_index():
    url = "http://seec.ct.gov/eCrisHome/eCRIS_Search/PreviousYears"
    return st.get(url)

def seec_url_to_filename(url):
    junk = "http://seec.ct.gov/ecrisreporting/Data/eCrisDownloads/ExportDataFiles/"
    return os.path.join(out_dir, url[len(junk):])

make_directories()
st.get_files(get_seec_index(),fname=seec_url_to_filename)
