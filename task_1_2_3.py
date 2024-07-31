"""Завдання 1.
Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому 
дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту 
чи з іншого джерела.

Завдання 2.
Напишіть алгоритм (функцію), який знаходить найменше значення у двійковому 
дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з 
конспекту чи з іншого джерела.

Завдання 3.
Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому 
дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з 
конспекту чи з іншого джерела."""

class Node:
    # Ініціалізуємо вузол дерева з заданим значенням ключа
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        # Рекурсивний метод для виводу дерева у вигляді рядка
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    # Вставляє новий вузол з заданим ключем в дерево
    if root is None:
        return Node(key)  # Якщо дерево порожнє, створюємо новий вузол
    else:
        if key < root.val:
            root.left = insert(root.left, key)  # Вставляємо в ліву піддерево
        else:
            root.right = insert(root.right, key)  # Вставляємо в праву піддерево
    return root

def search(root, key):
    # Пошук вузла з заданим ключем в дереві
    if root is None or root.val == key:
        return root  # Повертаємо вузол, якщо знайдено, або None, якщо не знайдено
    if key < root.val:
        return search(root.left, key)  # Шукаємо в лівому піддереві
    return search(root.right, key)  # Шукаємо в правому піддереві

def min_value_node(node):
    # Знаходить вузол з найменшим значенням в дереві
    current = node
    while current.left:
        current = current.left  # Йдемо вліво до кінця
    return current

def max_value_node(node):
    # Знаходить вузол з найбільшим значенням в дереві
    current = node
    while current.right:
        current = current.right  # Йдемо вправо до кінця
    return current

def sum_values(node):
    # Обчислює суму всіх значень в дереві
    if node is None:
        return 0
    return node.val + sum_values(node.left) + sum_values(node.right)  # Рекурсивно додаємо значення всіх вузлів

def delete(root, key):
    # Видаляє вузол з заданим ключем з дерева
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)  # Видаляємо з лівого піддерева
    elif key > root.val:
        root.right = delete(root.right, key)  # Видаляємо з правого піддерева
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp  # Якщо немає лівого піддерева, повертаємо праве
        elif not root.right:
            temp = root.left
            root = None
            return temp  # Якщо немає правого піддерева, повертаємо ліве
        root.val = min_value_node(root.right).val  # Заміщуємо значення мінімальним з правого піддерева
        root.right = delete(root.right, root.val)  # Видаляємо мінімальний вузол у правому піддереві
    return root

# Створення дерева і вставка значень
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

# Вивід дерева
print(root)

# Знаходження та вивід найменшого та найбільшого значення в дереві
print("Найменше значення в дереві:", min_value_node(root).val)
print("Найбільше значення в дереві:", max_value_node(root).val)

# Обчислення та вивід суми всіх значень в дереві
print("Сума всіх значень в дереві:", sum_values(root))
