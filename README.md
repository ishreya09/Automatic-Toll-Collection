# Automatic-Toll-Collection



### **Training and Validation Losses:**
- **Box Loss** (`train/box_loss`, `val/box_loss`): Measures the error in bounding box predictions. The training box loss starts at 1.1072 and decreases to 0.53536 by epoch 50. Validation box loss shows a similar trend, starting at 1.0939 and decreasing to 0.68965 by epoch 50. This consistent decrease indicates that the model is improving in predicting bounding box coordinates.
  
- **Class Loss** (`train/cls_loss`, `val/cls_loss`): Measures the error in class predictions. The training class loss decreases from 1.4692 to 0.31531 by epoch 50. Validation class loss starts at 1.3829 and reduces to 0.38849. The reduction in class loss signifies better performance in classifying objects correctly.

- **DFL Loss** (`train/dfl_loss`, `val/dfl_loss`): Measures the distance from the predicted bounding box coordinates to the ground truth. The training DFL loss decreases from 1.3727 to 1.0006, while the validation DFL loss starts at 1.3806 and reduces to 0.38849. This indicates improvement in the refinement of bounding box predictions.

### **Metrics:**
- **Precision** (`metrics/precision(B)`): Indicates the proportion of true positive predictions among all positive predictions made by the model. Precision values range from 0.7923 to 0.97579. High precision values indicate that the model makes few false positive predictions.

- **Recall** (`metrics/recall(B)`): Indicates the proportion of true positive predictions among all actual positives in the dataset. Recall values range from 0.74737 to 0.89649. High recall values indicate that the model misses few true positives.

- **mAP50** (`metrics/mAP50(B)`): Mean Average Precision at IoU threshold 0.5. Values range from 0.7833 to 0.9382. Higher mAP50 values indicate better overall performance in detecting objects.

- **mAP50-95** (`metrics/mAP50-95(B)`): Mean Average Precision across multiple IoU thresholds (from 0.5 to 0.95). Values range from 0.54187 to 0.78595. This metric is more challenging, and the increasing trend indicates improved detection performance across different IoU thresholds.

### **Learning Rate** (`lr/pg0`, `lr/pg1`, `lr/pg2`):
- The learning rate gradually decreases from 0.0006653 at epoch 1 to 5.96e-05 at epoch 50. A decaying learning rate helps in fine-tuning the model parameters and stabilizes the training process towards the end.

### **Overall Insights:**
1. **Convergence:** The training and validation losses consistently decrease, indicating good convergence of the model.
2. **Performance:** The precision, recall, mAP50, and mAP50-95 metrics show improvement over epochs, signifying enhanced detection performance.
3. **Stability:** The decreasing learning rate helps in fine-tuning and achieving stable training towards the end.



### References

https://docs.ultralytics.com/usage/python/#export

Dataset - https://universe.roboflow.com/mochoye/license-plate-detector-ogxxg

```bibtex
@misc{
                            license-plate-detector-ogxxg_dataset,
                            title = { License Plate Detector Dataset },
                            type = { Open Source Dataset },
                            author = { Mochoye },
                            howpublished = { \url{ https://universe.roboflow.com/mochoye/license-plate-detector-ogxxg } },
                            url = { https://universe.roboflow.com/mochoye/license-plate-detector-ogxxg },
                            journal = { Roboflow Universe },
                            publisher = { Roboflow },
                            year = { 2023 },
                            month = { aug },
                            note = { visited on 2024-07-31 },
                            }
```

