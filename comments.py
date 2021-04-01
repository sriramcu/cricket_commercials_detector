# ~ parser.add_argument('-w', '--weights',
    # ~ type=str,
    # ~ default='./yolov3-coco/yolov3.weights',
    # ~ help='Path to the file which contains the weights \
    # ~ for YOLOv3.')

    # ~ parser.add_argument('-cfg', '--config',
    # ~ type=str,
    # ~ default='./yolov3-coco/yolov3.cfg',
    # ~ help='Path to the configuration file for the YOLOv3 model.')
    # ~ det = False
    # ~ if not skip_obj and label == "anomaly":
        # ~ net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

        # ~ # Get the output layer names of the model
        # ~ layer_names = net.getLayerNames()
        # ~ layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        
        # ~ blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), 
                            # ~ swapRB=True, crop=False)

        # ~ # Perform a forward pass of the YOLO object detector
        # ~ net.setInput(blob)

        # ~ # Getting the outputs from the output layers
        # ~ outs = net.forward(layer_names)
       
        # ~ classids = []
        # ~ my_labels = open('coco-labels').read().strip().split('\n')
        # ~ for out in outs:
            # ~ for detection in out:
               
                # ~ scores = detection[5:]
                # ~ classid = np.argmax(scores)
                # ~ confidence = scores[classid]
            
                
                # ~ # Consider only the predictions that are above a certain confidence level
                # ~ if confidence > tconf: #tconf is threshold 0-1
                    # ~ # TODO Check detection
                    # ~ classids.append(my_labels[classid])
                    
        
        
        
        # ~ classids = [x for x in classids if x in ["sports ball","baseball bat","baseball glove"]]
        # ~ if len(classids)>0:
            # ~ color = (122,122,122)
            # ~ print(classids)
            # ~ det = True
        # ~ all_class_ids = "".join(str(v) for v in classids)
        # ~ cv2.putText(image, all_class_ids, (10,  50), cv2.FONT_HERSHEY_SIMPLEX,0.7, color, 2)
    
    
    
    # ~ if det:
        # ~ cv2.imwrite("specialop{}.jpg".format(time.time()), image) 
        # ~ print("Image saved")
        
    # draw the predicted label text on the original image
