This Streamlit application provides a graphical interface to interact with AVL and Splay trees. Users can insert, delete, splay (for Splay trees), and visualize the structure of the trees dynamically.

**Features**
  
   Tree Types Supported: AVL Tree and Splay Tree.

  
**Operations:**


    Insert a node.
    Delete a node.
    Splay a node (Splay Tree only).
    Display the current structure of the tree.
    Dynamic Visualization: The tree structure updates and displays after each operation

  
**How to Use**


    Select Tree Type: Choose between AVL Tree or Splay Tree using the dropdown menu.
    Choose an Operation:
    Insert: Add a new key to the selected tree.
    Delete: Remove a key from the selected tree.
    Splay Node: Available only for Splay Tree. Moves the selected key to the root.
    Display: Visualizes the current structure of the selected tree.
    Enter Key: Input the numeric key for the chosen operation.
    Execute Operation: Click the "Execute" button to perform the operation.

    
**Error Handling**

      Empty Tree: If you try to display or perform operations on an empty tree, an error message will be shown.
      Invalid Splay Operation: Attempting to splay a node in an AVL Tree or a non-existent node in a Splay Tree will display appropriate error messages.

    
**Prerequisites**

    Python 3.7+
     Required Python libraries:
        streamlit
        matplotlib

To run it in Windows: python -m streamlit run visual.py
