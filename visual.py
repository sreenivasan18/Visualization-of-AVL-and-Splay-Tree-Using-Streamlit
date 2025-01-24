import streamlit as st
import matplotlib.pyplot as plt

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right)) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)
        balance = self.balance(root)

        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left or not root.right:
                return root.left if root.left else root.right
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        self.update_height(root)
        balance = self.balance(root)

        if balance > 1:
            if self.balance(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if self.balance(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def maximum(self, x):
        while x.right:
            x = x.right
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x.parent.left == x:
                    self.right_rotate(x.parent)
                else:
                    self.left_rotate(x.parent)
            elif x.parent.left == x and x.parent.parent.left == x.parent:
                self.right_rotate(x.parent.parent)
                self.right_rotate(x.parent)
            elif x.parent.right == x and x.parent.parent.right == x.parent:
                self.left_rotate(x.parent.parent)
                self.left_rotate(x.parent)
            elif x.parent.left == x and x.parent.parent.right == x.parent:
                self.right_rotate(x.parent)
                self.left_rotate(x.parent.parent)
            else:
                self.left_rotate(x.parent)
                self.right_rotate(x.parent.parent)

    def insert(self, key):
        node = Node(key)
        y = None
        x = self.root
        while x:
            y = x
            if key < x.data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if not y:
            self.root = node
        elif key < y.data:
            y.left = node
        else:
            y.right = node
        self.splay(node)

    def search(self, key):
        x = self.root
        while x:
            if x.data == key:
                self.splay(x)
                return x
            elif key < x.data:
                x = x.left
            else:
                x = x.right
        return None

    def delete(self, key):
        node = self.search(key)
        if node:
            self.splay(node)
            if not node.left:
                self.root = node.right
                if self.root:
                    self.root.parent = None
            elif not node.right:
                self.root = node.left
                if self.root:
                    self.root.parent = None
            else:
                max_left = self.maximum(node.left)
                self.splay(max_left)
                self.root.right = node.right
                node.right.parent = self.root

    def maximum(self, x):
        while x.right:
            x = x.right
        return x

def visualize_tree(tree, is_avl=True):
    def draw_node(ax, node, x, y, dx, is_avl):
        if not node:
            return
        ax.text(x, y, str(node.key if is_avl else node.data), fontsize=12, ha='center',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))
        if node.left:
            ax.plot([x, x - dx], [y, y - 1], 'k-')
            draw_node(ax, node.left, x - dx, y - 1, dx / 2, is_avl)
        if node.right:
            ax.plot([x, x + dx], [y, y - 1], 'k-')
            draw_node(ax, node.right, x + dx, y - 1, dx / 2, is_avl)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 1)
    ax.axis('off')

    if tree.root:
        draw_node(ax, tree.root, 0, 0, 5, is_avl)

    plt.tight_layout()
    return fig

st.title("Tree Visualization: AVL and Splay Trees")
st.write("Use the options below to visualize AVL and Splay Tree operations.")

tree_type = st.selectbox("Choose the Tree Type:", ["AVL Tree", "Splay Tree"])

if "avl_tree" not in st.session_state:
    st.session_state.avl_tree = AVLTree()
if "splay_tree" not in st.session_state:
    st.session_state.splay_tree = SplayTree()

tree = st.session_state.avl_tree if tree_type == "AVL Tree" else st.session_state.splay_tree

action = st.radio("Choose an operation:", ["Insert", "Delete", "Splay Node", "Display"])
key = st.number_input("Enter a key:", min_value=0, step=1, value=0)

if st.button("Execute"):
    if action == "Insert":
        if tree_type == "AVL Tree":
            tree.root = tree.insert(tree.root, key)
        else:
            tree.insert(key)
        st.success(f"Inserted {key} into {tree_type}.")
    elif action == "Delete":
        if tree_type == "AVL Tree":
            tree.root = tree.delete(tree.root, key)
        else:
            tree.delete(key)
        st.success(f"Deleted {key} from {tree_type}.")
    elif action == "Splay Node":
        if tree_type == "Splay Tree":
            result = tree.search(key)
            if result:
                st.success(f"Splayed node with key {key} in the Splay Tree.")
            else:
                st.error(f"Key {key} not found in the Splay Tree.")
        else:
            st.error("Splay operation is not supported for AVL Trees.")
    elif action == "Display":
        if not tree.root:
            st.error(f"The {tree_type} is empty. Please insert nodes first.")
        else:
            fig = visualize_tree(tree, is_avl=(tree_type == "AVL Tree"))
            st.pyplot(fig)
