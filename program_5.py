def course_info():
    course_dict = {}

    while True:
        course_id = input("Enter course ID (or 'done' when complete): ")
        if course_id.lower() == 'done':
            break
        course_name = input("Enter course name: ")
        course_dict[course_id] = course_name

    subject = input("Enter the subject to search for: ")

    print("Courses found:")
    for course_id, course_name in course_dict.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")

if __name__ == "__main__":
    course_info()
