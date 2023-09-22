from datasets import load_dataset
import json

task_list = [
    "computer_network",
    "operating_system",
    "computer_architecture",
    "college_programming",
    "college_physics",
    "college_chemistry",
    "advanced_mathematics",
    "probability_and_statistics",
    "discrete_mathematics",
    "electrical_engineer",
    "metrology_engineer",
    "high_school_mathematics",
    "high_school_physics",
    "high_school_chemistry",
    "high_school_biology",
    "middle_school_mathematics",
    "middle_school_biology",
    "middle_school_physics",
    "middle_school_chemistry",
    "veterinary_medicine",
    "college_economics",
    "business_administration",
    "marxism",
    "mao_zedong_thought",
    "education_science",
    "teacher_qualification",
    "high_school_politics",
    "high_school_geography",
    "middle_school_politics",
    "middle_school_geography",
    "modern_chinese_history",
    "ideological_and_moral_cultivation",
    "logic",
    "law",
    "chinese_language_and_literature",
    "art_studies",
    "professional_tour_guide",
    "legal_professional",
    "high_school_chinese",
    "high_school_history",
    "middle_school_history",
    "civil_servant",
    "sports_science",
    "plant_protection",
    "basic_medicine",
    "clinical_medicine",
    "urban_and_rural_planner",
    "accountant",
    "fire_engineer",
    "environmental_impact_assessment_engineer",
    "tax_accountant",
    "physician",
]

# Tạo một danh sách để lưu trữ tất cả dữ liệu từ các task
all_data = []

for task_name in task_list:
    dataset = load_dataset("ceval/ceval-exam", name=task_name)

    # Lặp lại 50 lần để trích xuất 50 giá trị cho mỗi task_name
    for i in range(50):
        data = dataset['test'][i] 

        # Trích xuất thông tin cần thiết
        question = data['question']
        choices = [data['A'], data['B'], data['C'], data['D']]
        answer = data['answer']
        explanation = data['explanation']

        # Tạo một từ điển chứa thông tin
        entry = {
            'question': question,
            'A': choices[0],
            'B': choices[1],
            'C': choices[2],
            'D': choices[3],
            'answer': answer,
            'explanation': explanation,
            'category_type': task_name,
        }

        # Thêm từ điển này vào danh sách tất cả dữ liệu
        all_data.append(entry)

# Lưu danh sách dữ liệu vào một tệp JSON
with open('c-eval.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=4)
