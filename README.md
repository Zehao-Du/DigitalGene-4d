# 🧬 Digital Gene Infrastructure

## 🏛️ About Digital Gene Infrastructure and Analytic Concepts

Digital Gene Infrastructure is built upon analytic concepts, including

- Fully-parameterized object representation
- Procedural generation of novel and diverse objects
- Automated object function analysis and manipulation manual

## 🚀 Highlights

### **Fully-parameterized Object Representation**

Using a carefully designed annotation system with program templates, real-world objects can be converted to a fully-parameterized representation with minor effort.

<p align="center">
<img src="assets\videos\digital-gene-annotation.gif" width="100%"/>
</p>

### **Procedural Generation of Novel and Diverse Objects**

By sampling parameters that adheres to physical constraints as well as common sense, countless new objects can be procedurally generated using templates.

<p align="center">
<img src="assets\videos\procedural-generation.gif" width="100%"/>
</p>

### **Automated Object Function Analysis and Manipulation Manual**

Parameterized defintion of knowledge is supported, including segmentation, 6D pose as well as affordances. In a comprehensive way, these knowledge lays the foundation of interpretable and controllable object manipulation.

<p align="center">
<img src="assets\videos\Mug-segment.gif" width="18%"/>
<img src="assets\videos\Mug-open_lid.gif" width="18%"/>
<img src="assets\videos\Mug-containment.gif" width="18%"/>
<img src="assets\videos\Mug-joint-pose.gif" width="18%"/>
<img src="assets\videos\Mug-grasp.gif" width="18%"/>
</p>
<p align="center">
<img src="assets\videos\knowledge-1.gif" width="30%"/>
<img src="assets\videos\knowledge-2.gif" width="30%"/>
<img src="assets\videos\knowledge-3.gif" width="30%"/>
</p>


## 🔧 Setup & Dependencies

> Python 3.8+ is recommended.

Install dependencies via pip:

```bash
pip install -r requirements.txt
```


## 🚀 Usage

### 1. Standard Concept Template Library (STLC)

For each object category, download the corresponding conceptualization result file from this folder:

📎 [STLC Conceptualizations on Google Drive](https://drive.google.com/drive/folders/18fTrisH-9psUWRe8zdt4dPAyv1K4twxz)

**Steps:**

1. Download the file named `{CATEGORY_NAME}_conceptualization.pkl`
2. Rename it to `{CATEGORY_NAME}.pkl`
3. Move it to: `assets/conceptualizations/stlc/`
4. [Optional] If you want to visualize both the actual object and the conceptualization results simultaneously, you can download the data from the corresponding dataset (the data IDs match one-to-one with the original dataset). Then, place the downloaded OBJ files in the folder `assets/object_models/{CATEGORY_NAME}`.

Then run:

```bash
cd Digital-Gene-Toolkit
python stlc_visualize.py --category {CATEGORY_NAME}
```

### 2. Procedural Generation

You can procedurally generate new conceptualizations and visualize them by running:

```bash
cd Digital-Gene-Toolkit
python prog_visualize.py --category {CATEGORY_NAME} --gen_num {GEN_NUM}
```

- `{CATEGORY_NAME}`: object category nam
- `{GEN_NUM}`: number of generated samples

The output will be saved as:
`assets/conceptualizations/prog/{CATEGORY_NAME}.pkl`


### 3. Concept Knowledge

This module generates knowledge visualizations based on procedurally generated data.

Ensure that the corresponding `{CATEGORY_NAME}.pkl` file already exists in `assets/conceptualizations/prog/`, and then run:

```bash
cd Digital-Gene-Toolkit
python knowledge_visualize.py --category {CATEGORY_NAME}
```

The output GIFs will be saved in the `output_gifs` directory.


## 🙏 Acknowledgement

### 🖥️ **Annotation System Contributions**

 - `Function Design`: Longfei Xu, Yuxuan Li, Nange Wang
 - `Template Design`: Longfei Xu, Nange Wang, Yuxuan Li, Yining Zhang
 - `Workflow Design`: Yuxuan Li, Longfei Xu
 - `Interface Design`: Longfei Xu, Yuxuan Li


### ⌨️ **Code Contributions**

 - `Template Design`: Nange Wang, Longfei Xu, Yuxuan Li, Yining Zhang
 - `Knowledge Design`: Yixuan Jiang, Jiude Wei
 - `Procedural Generation`: Jiude Wei, Yuxuan Li, Xuzhou Zhu, Tianyu Shen, Jiangjiyuan Wang


### 📽️ **Video Contributions**
 - `Video Producer`: Jiude Wei, Longfei Xu, and Mingyang Sun
 - `Video Clip`: Jian Zhang
 - `Digital Gene Program Modelling`: Jiude Wei and Nange Wang
 - `Digital Gene Visualization`: Longfei Xu, Jiude Wei, Qichen He and Yi Yang
 - `Robot Motion Developer`: Jiude Wei, Mingyang Sun, Jiacheng Liu, Xinyu Zhou, Qichen He, Yi Yang and Xinyu Zhang
 - `Real-world Scanning`: Qichen He and Yi Yang
 - `Other Material Providers`: Yuxuan Li, Jiachun Bao, Yixuan Jiang and Zhipeng Zhou


## 🖋️ Citation

The idea for this project originates from the following papers.

```bibtex
@article{sun2025digital,
  title={Digital Gene: Learning about the Physical World through Analytic Concepts},
  author={Sun, Jianhua and Lu, Cewu},
  journal={arXiv preprint arXiv:2504.04170},
  year={2025}
}

@article{sun2024conceptfactory,
  title={Conceptfactory: Facilitate 3d object knowledge annotation with object conceptualization},
  author={Sun, Jianhua and Li, Yuxuan and Xu, Longfei and Wang, Nange and Wei, Jiude and Zhang, Yining and Lu, Cewu},
  journal={Advances in Neural Information Processing Systems},
  volume={37},
  pages={75454--75467},
  year={2024}
}

@article{sun2024arti,
  title={Arti-PG: A Toolbox for Procedurally Synthesizing Large-Scale and Diverse Articulated Objects with Rich Annotations},
  author={Sun, Jianhua and Li, Yuxuan and Wei, Jiude and Xu, Longfei and Wang, Nange and Zhang, Yining and Lu, Cewu},
  journal={arXiv e-prints},
  pages={arXiv--2412},
  year={2024}
}

@inproceedings{sun2025discovering,
  title={Discovering conceptual knowledge with analytic ontology templates for articulated objects},
  author={Sun, Jianhua and Li, Yuxuan and Xu, Longfei and Wei, Jiude and Chai, Liang and Lu, Cewu},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={39},
  number={14},
  pages={14681--14689},
  year={2025}
}
```

