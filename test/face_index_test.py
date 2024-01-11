from typing import List


def main():

    faces_index: List[int] = [0, 1]
    print(f"faces_index={faces_index}")

    for i in range(2):
        target_face_index: List[int] = [0]
        target_face_index[0] = faces_index[i] if len(faces_index) > 1 else faces_index[0]
        print(f"target_face_index={target_face_index}")


if __name__ == '__main__':
    main()
