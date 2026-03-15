import os
import time
import subprocess

# Paths
CV_DIR = os.path.dirname(os.path.abspath(__file__))
TECTONIC_PATH = os.path.expanduser("~/miniconda3/envs/latex_env/bin/tectonic")
RESUME_EN = os.path.join(CV_DIR, "resume_en.tex")
RESUME_CN = os.path.join(CV_DIR, "resume_cn.tex")
COMBINED_PDF = os.path.join(CV_DIR, "resume_combined.pdf")

def compile_tex(filepath):
    print(f"[{time.strftime('%H:%M:%S')}] Compiling {os.path.basename(filepath)}...")
    try:
        subprocess.run([TECTONIC_PATH, filepath], check=True, cwd=CV_DIR)
        print(f"[{time.strftime('%H:%M:%S')}] Successfully compiled {os.path.basename(filepath)}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[{time.strftime('%H:%M:%S')}] Error compiling {os.path.basename(filepath)}: {e}")
        return False

def merge_pdfs():
    print(f"[{time.strftime('%H:%M:%S')}] Merging PDFs...")
    try:
        en_pdf = RESUME_EN.replace(".tex", ".pdf")
        cn_pdf = RESUME_CN.replace(".tex", ".pdf")
        subprocess.run(["pdfunite", en_pdf, cn_pdf, COMBINED_PDF], check=True, cwd=CV_DIR)
        print(f"[{time.strftime('%H:%M:%S')}] Successfully generated {os.path.basename(COMBINED_PDF)}")
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Error merging PDFs: {e}")

def main():
    print("CV Auto-compiler started. Watching for changes in .tex files...")
    
    last_mtimes = {
        RESUME_EN: os.path.getmtime(RESUME_EN) if os.path.exists(RESUME_EN) else 0,
        RESUME_CN: os.path.getmtime(RESUME_CN) if os.path.exists(RESUME_CN) else 0
    }

    try:
        while True:
            changed = False
            for tex_file in [RESUME_EN, RESUME_CN]:
                if os.path.exists(tex_file):
                    current_mtime = os.path.getmtime(tex_file)
                    if current_mtime > last_mtimes[tex_file]:
                        print(f"Detected change in {os.path.basename(tex_file)}")
                        if compile_tex(tex_file):
                            changed = True
                        last_mtimes[tex_file] = current_mtime
            
            if changed:
                merge_pdfs()
            
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopping CV Auto-compiler.")

if __name__ == "__main__":
    main()
