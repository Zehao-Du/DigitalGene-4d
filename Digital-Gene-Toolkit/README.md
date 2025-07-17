# 🧬 Digital Gene Toolkit


## 🔧 Setup & Dependencies

> Python 3.8+ is recommended.

Install dependencies via pip:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Standard Concept Template Library (STLC)

For each object category, download the corresponding conceptualization result file from this folder:

📎 [STLC Conceptualizations on Google Drive](https://drive.google.com/drive/folders/18fTrisH-9psUWRe8zdt4dPAyv1K4twxz)

**Steps:**

1. Download the file named `{CATEGORY_NAME}_conceptualization.pkl`
2. Rename it to `{CATEGORY_NAME}.pkl`
3. Move it to: `assets/conceptualizations/stlc/`

Then run:

```bash
python stlc_visualize.py --category {CATEGORY_NAME}
```

---

### 2. Procedural Generation (PROG)

You can procedurally generate new conceptualizations and visualize them by running:

```bash
python prog_visualize.py --category {CATEGORY_NAME} --gen_num {GEN_NUM}
```

- `{CATEGORY_NAME}`: object category nam
- `{GEN_NUM}`: number of generated samples

The output will be saved as:
`assets/conceptualizations/prog/{CATEGORY_NAME}.pkl`

---

### 3. Digital Gene Knowledge

This module generates knowledge visualizations based on procedurally generated data.

Ensure that the corresponding `{CATEGORY_NAME}.pkl` file already exists in `assets/conceptualizations/prog/`, and then run:

```bash
python knowledge_visualize.py --category {CATEGORY_NAME}
```

The output GIFs will be saved in the `output_gifs` directory.