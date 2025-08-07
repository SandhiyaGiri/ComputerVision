# Binary Fracture Detection with EfficientDet

A PyTorch Lightning-based training script for binary fracture detection using EfficientDet models. This script trains a model to classify medical images as either containing fractures or post-operative conditions.

## Features

- **Binary Classification**: Distinguishes between fracture and post-operative images
- **Label Filtering**: Automatically excludes annotations with specific medical terms that don't represent fractures
- **Robust Data Handling**: Handles corrupted images gracefully and logs them for review
- **Medical Image Optimization**: Uses custom normalization constants optimized for medical X-ray images
- **Comprehensive Evaluation**: Provides detailed metrics and sorts test images into TP, FP, TN, FN folders
- **Flexible Data Splitting**: Ensures unbiased test sets with configurable train/validation/test splits
- **Mixed Precision Training**: Optimized for modern GPUs with automatic mixed precision

## Key Components

### Label Management
- **Excluded Labels**: Automatically filters out non-fracture medical conditions like dislocations, calcifications, etc.
- **Post-op Classification**: Identifies post-operative conditions and classifies them separately from fractures
- **Binary Classes**: 
  - Class 1: Fracture
  - Class 2: Post-operative

### Data Processing
- **Medical Image Normalization**: Uses custom mean/std values optimized for X-ray images
- **Robust BBox Handling**: Validates and filters bounding boxes to ensure training stability
- **Corrupted Image Handling**: Logs and skips corrupted images without crashing the training

## Requirements

```bash
pip install torch torchvision
pip install pytorch-lightning
pip install effdet
pip install albumentations
pip install wandb
pip install pandas numpy pillow tqdm
```

## Usage

### Basic Training

```bash
python train_effdet_binary.py \
    --data_dir /path/to/data \
    --csv_path /path/to/annotations.csv \
    --model_name tf_efficientdet_d0 \
    --batch_size 16 \
    --max_epochs 20 \
    --normal_limit 1000
```

### Advanced Training

```bash
python train_effdet_binary.py \
    --data_dir /home/ai-user/multi-shoulder/Data \
    --csv_path /home/ai-user/multi-shoulder/fracture.csv \
    --model_name tf_efficientdet_d7x \
    --batch_size 2 \
    --max_epochs 50 \
    --normal_limit 5000 \
    --learning_rate 1e-4 \
    --test_size 200
```

## Command Line Arguments

### Data Parameters
- `--data_dir`: Path to data directory containing fracture/ and normal/ subdirectories
- `--csv_path`: Path to annotations CSV file
- `--normal_limit`: Maximum number of normal images for training (default: 5000)
- `--test_size`: Number of images per class for testing (default: 200)

### Model Parameters
- `--model_name`: EfficientDet model variant (default: tf_efficientdet_d7x)
- `--batch_size`: Training batch size (default: 2)
- `--learning_rate`: Learning rate (default: 1e-4)

### Training Parameters
- `--max_epochs`: Maximum training epochs (default: 50)
- `--num_workers`: Number of DataLoader workers (auto-detected if None)

### Evaluation Parameters
- `--no_evaluation`: Skip evaluation after training (default: True)
- `--eval_conf_threshold`: Confidence threshold for evaluation (default: 0.3)
- `--eval_iou_threshold`: IoU threshold for evaluation (informational, default: 0.5)
- `--eval_seed`: Random seed for reproducible data splits (default: 42)

## Data Structure

```
data_dir/
├── fracture/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── normal/
    ├── image1.jpg
    ├── image2.jpg
    └── ...
```

## CSV Format

The annotations CSV should contain:
- `study_path`: Image identifier/path
- `bbox`: JSON string containing bounding box annotations

Example:
```csv
study_path,bbox
image1,"[{'x': 25, 'y': 30, 'width': 15, 'height': 20, 'rectanglelabels': ['fracture']}]"
```

## Output

### Training Artifacts
- Model checkpoints saved in `runs_binary_effdet_5000_normal/{model_name}_{timestamp}/`
- Best model based on validation loss
- Training logs via Weights & Biases

### Evaluation Results
When evaluation is enabled, the script provides:
- **Metrics**: Accuracy, Precision, Recall, F1-Score, Specificity
- **Sorted Images**: Test images organized into TP, FP, TN, FN folders
- **Detailed Logs**: Corrupted image log and invalid bounding box log

### Log Files
- `corrupted_images_binary.txt`: Log of corrupted images encountered
- `invalid_bboxes_binary_{timestamp}.txt`: Log of invalid bounding boxes

## Model Architecture

The script uses EfficientDet with:
- **Backbone**: EfficientNet (configurable variants D0-D7X)
- **Detection Head**: Custom classification head for binary detection
- **Input Size**: Automatically determined from model configuration
- **Normalization**: Medical image-specific normalization constants

## Training Features

- **Mixed Precision**: Automatic mixed precision training for GPU efficiency
- **Gradient Accumulation**: Effective batch size = batch_size × 3
- **Early Stopping**: Stops training if validation loss doesn't improve for 8 epochs
- **Learning Rate Scheduling**: ReduceLROnPlateau with patience=3
- **Gradient Clipping**: Clips gradients at 10.0 to prevent exploding gradients

## Medical Image Considerations

- **Custom Normalization**: Uses medical image-specific mean/std values
- **Data Augmentation**: Horizontal flips, brightness/contrast adjustments, blur effects
- **Label Filtering**: Excludes non-fracture medical conditions
- **Robust Validation**: Handles various image formats and potential corruption

## Performance Optimization

- **Tensor Core Optimization**: Uses medium precision for A100 GPUs
- **Memory Efficiency**: Gradient accumulation for larger effective batch sizes
- **Multi-worker Loading**: Configurable number of DataLoader workers
- **Mixed Precision**: Automatic mixed precision training

## Troubleshooting

### Common Issues

1. **Out of Memory**: Reduce batch_size or enable gradient accumulation
2. **Corrupted Images**: Check the corrupted_images_binary.txt log
3. **Invalid BBox**: Review invalid_bboxes_binary_{timestamp}.txt
4. **Slow Training**: Adjust num_workers or use smaller model variant

### Debugging

- Enable evaluation with `--no_evaluation False`
- Check logs in the output directory
- Monitor training progress via Weights & Biases

## License

This code is provided for research and educational purposes. Please ensure compliance with relevant medical data privacy regulations when using this script with patient data. 
