import os
import numpy as np
import glob

def load_annotations(annotation_dir):
    annotations = []
    
    for file_path in glob.glob(os.path.join(annotation_dir, "*.txt")):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            annotations.extend(lines)
            print(annotations)
    
    return annotations

def undersample_data(annotation_dir, undersample_ratio):
    annotations = load_annotations(annotation_dir)
    
    label_counts = {}
    for annotation in annotations:
        label = annotation.split()[0]
        if label not in label_counts:
            label_counts[label] = 0
        label_counts[label] += 1
    
    min_label_count = min(label_counts.values())
    undersample_count = int(min_label_count * undersample_ratio)
    
    undersampled_annotations = []
    for annotation in annotations:
        label = annotation.split()[0]
        if label_counts[label] > undersample_count:
            undersampled_annotations.append(annotation)
            label_counts[label] -= 1
    
    return undersampled_annotations

def get_original_annotation_list(annotation_dir, undersample_ratio):
    original_annotations = load_annotations(annotation_dir)
    undersampled_annotations = undersample_data(annotation_dir, undersample_ratio)
    
    original_annotation_list = []
    for annotation in original_annotations:
        if annotation in undersampled_annotations:
            original_annotation_list.append(annotation)
    
    return original_annotation_list

def save_original_annotation_list(annotation_dir, output_file, undersample_ratio):
    original_annotations = get_original_annotation_list(annotation_dir, undersample_ratio)
    
    with open(output_file, 'w') as file:
        for annotation in original_annotations:
            file.write(annotation)

annotation_dir = './dataset/train/labels'
output_file = "./undersampling_file.txt"
undersample_ratio = 0.5

save_original_annotation_list(annotation_dir, output_file, undersample_ratio)