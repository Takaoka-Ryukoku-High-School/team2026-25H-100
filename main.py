import json
from datetime import date, timedelta
from pathlib import Path
from uuid import uuid4

import flet as ft


DATA_FILE = Path.home() / ".classroom_board.json"
GREEN = "#315C4C"
GREEN_LIGHT = "#E8F0E9"
PAPER = "#F5F5F0"
INK = "#26332E"
MUTED = "#7B8580"
LINE = "#E4E7E1"
ORANGE = "#B86A35"
CLASS_GROUPS = {
    "1年生": [f"{number}組" for number in range(1, 8)],
    "2年生": [
        *(f"{number}組" for number in range(1, 8)),
        "アートコース",
        "L&Sコース",
        "デジタルコース",
    ],
    "3年生": [f"{number}組" for number in range(1, 7)],
}
CLASS_SUBJECTS = {
    ("2年生", "アートコース"): [
        ("2-art-comic-art", "コミックアート"),
        ("2-art-digital-art", "デジタルアート"),
        ("2-art-management", "アートマネジメント"),
    ],
    ("2年生", "3組"): [
        ("2-3-classical-inquiry", "古典探求"),
        ("2-3-logical-japanese", "論理国語"),
        ("2-3-math-a", "数学A"),
        ("2-3-logical-expression-1", "論理表現Ⅰ"),
        ("2-3-civics", "公共"),
        ("2-3-geography-synthesis", "地理総合"),
        ("2-3-basic-chemistry", "化学基礎"),
        ("2-3-information-2", "情報Ⅱ"),
        ("2-3-human-studies", "人間学"),
        ("2-3-health", "保健"),
        ("2-3-physical-education", "体育"),
    ],
    ("2年生", "4組"): [
        ("2-4-classical-inquiry", "古典探求"),
        ("2-4-logical-japanese", "論理国語"),
        ("2-4-math-a", "数学A"),
        ("2-4-logical-expression-1", "論理表現Ⅰ"),
        ("2-4-civics", "公共"),
        ("2-4-geography-synthesis", "地理総合"),
        ("2-4-basic-chemistry", "化学基礎"),
        ("2-4-information-2", "情報Ⅱ"),
        ("2-4-human-studies", "人間学"),
        ("2-4-health", "保健"),
        ("2-4-physical-education", "体育"),
    ],
    ("2年生", "5組"): [
        ("2-5-classical-inquiry", "古典探求"),
        ("2-5-logical-japanese", "論理国語"),
        ("2-5-math-a", "数学A"),
        ("2-5-logical-expression-1", "論理表現Ⅰ"),
        ("2-5-civics", "公共"),
        ("2-5-geography-synthesis", "地理総合"),
        ("2-5-basic-chemistry", "化学基礎"),
        ("2-5-information-2", "情報Ⅱ"),
        ("2-5-human-studies", "人間学"),
        ("2-5-health", "保健"),
        ("2-5-physical-education", "体育"),
    ],
    ("2年生", "6組"): [
        ("2-6-classical-inquiry", "古典探求"),
        ("2-6-logical-japanese", "論理国語"),
        ("2-6-math-a", "数学A"),
        ("2-6-logical-expression-1", "論理表現Ⅰ"),
        ("2-6-civics", "公共"),
        ("2-6-geography-synthesis", "地理総合"),
        ("2-6-basic-chemistry", "化学基礎"),
        ("2-6-information-2", "情報Ⅱ"),
        ("2-6-human-studies", "人間学"),
        ("2-6-health", "保健"),
        ("2-6-physical-education", "体育"),
    ],
    ("2年生", "7組"): [
        ("2-7-classical-inquiry", "古典探求"),
        ("2-7-logical-japanese", "論理国語"),
        ("2-7-math-a", "数学A"),
        ("2-7-logical-expression-1", "論理表現Ⅰ"),
        ("2-7-civics", "公共"),
        ("2-7-geography-synthesis", "地理総合"),
        ("2-7-basic-chemistry", "化学基礎"),
        ("2-7-information-2", "情報Ⅱ"),
        ("2-7-human-studies", "人間学"),
        ("2-7-health", "保健"),
        ("2-7-physical-education", "体育"),
    ],
}


def starter_data():
    today = date.today()
    subjects = [
        {"id": "math", "name": "数学 I"},
        {"id": "english", "name": "英語コミュニケーション"},
        {"id": "japanese", "name": "現代の国語"},
    ]
    return {
        "subjects": subjects,
        "records": [
            {
                "id": str(uuid4()),
                "subject_id": "math",
                "grade": "1年生",
                "class_name": "1組",
                "kind": "test",
                "title": "第2回定期考査",
                "date": (today + timedelta(days=8)).isoformat(),
                "detail": "教科書 p.42〜78 / 問題集 p.30〜45",
                "done": False,
            },
            {
                "id": str(uuid4()),
                "subject_id": "english",
                "grade": "1年生",
                "class_name": "1組",
                "kind": "assignment",
                "title": "Lesson 5 ワーク提出",
                "date": (today + timedelta(days=3)).isoformat(),
                "detail": "ワーク p.54〜61。丸つけをして提出。",
                "done": False,
            },
            {
                "id": str(uuid4()),
                "subject_id": "japanese",
                "grade": "1年生",
                "class_name": "1組",
                "kind": "progress",
                "title": "小説「羅生門」",
                "date": today.isoformat(),
                "detail": "本文の読解と登場人物の心情を確認。次回は語句の小テスト。",
                "done": False,
            },
        ],
    }


def load_data():
    if not DATA_FILE.exists():
        data = starter_data()
        DATA_FILE.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return data

    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("保存データの形式が正しくありません。")
    subjects = data.get("subjects")
    records = data.get("records")
    if not isinstance(subjects, list) or not isinstance(records, list):
        raise ValueError("保存データに科目または共有情報がありません。")
    if any(
        not isinstance(subject, dict)
        or not isinstance(subject.get("id"), str)
        or not isinstance(subject.get("name"), str)
        for subject in subjects
    ):
        raise ValueError("保存データの科目情報を読み込めません。")
    if any(
        not isinstance(record, dict)
        or not isinstance(record.get("id"), str)
        or not isinstance(record.get("subject_id"), str)
        or record.get("kind") not in {"test", "assignment", "progress"}
        or not isinstance(record.get("title"), str)
        or not isinstance(record.get("date"), str)
        or not isinstance(record.get("detail"), str)
        or not isinstance(record.get("done"), bool)
        for record in records
    ):
        raise ValueError("保存データの共有情報を読み込めません。")
    migrated = False
    for record in records:
        if "grade" not in record:
            record["grade"] = "1年生"
            migrated = True
        if "class_name" not in record:
            record["class_name"] = "1組"
            migrated = True
        if not isinstance(record["grade"], str) or not isinstance(
            record["class_name"], str
        ):
            raise ValueError("保存データの学年・クラス情報を読み込めません。")
    if migrated:
        DATA_FILE.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    return data


def main(page: ft.Page):
    page.title = "クラスボード | 授業の共有"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = PAPER
    page.padding = 24
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    data = load_data()
    subjects = data["subjects"]
    records = data["records"]
    selected_grade = "1年生"
    selected_class = CLASS_GROUPS[selected_grade][0]
    selected_subject = subjects[0]["id"] if subjects else ""
    current_view = "overview"
    form_open = False
    editing_id = None
    fields = []
    status_text = ft.Text("", size=12, color=ORANGE)
    body = ft.Column(spacing=16)

    view_labels = {
        "overview": "全体",
        "test": "テスト範囲",
        "assignment": "提出物",
        "progress": "授業の進度",
    }

    def current_subjects():
        scoped_names = CLASS_SUBJECTS.get((selected_grade, selected_class))
        if scoped_names is None:
            scoped_subject_ids = {
                subject_id
                for configured_subjects in CLASS_SUBJECTS.values()
                for subject_id, _ in configured_subjects
            }
            return [
                subject for subject in subjects if subject["id"] not in scoped_subject_ids
            ]
        scoped_subjects = []
        for subject_id, name in scoped_names:
            subject = next(
                (item for item in subjects if item["id"] == subject_id), None
            )
            if subject is None:
                subject = {"id": subject_id, "name": name}
                subjects.append(subject)
            scoped_subjects.append(subject)
        return scoped_subjects

    def ensure_selected_subject():
        nonlocal selected_subject
        available_subjects = current_subjects()
        if not any(item["id"] == selected_subject for item in available_subjects):
            selected_subject = available_subjects[0]["id"] if available_subjects else ""

    ensure_selected_subject()

    def persist():
        try:
            DATA_FILE.write_text(
                json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
            )
        except OSError as error:
            status_text.value = f"保存できませんでした: {error}"
            status_text.color = ORANGE
            page.update()
            return False
        status_text.value = "変更を保存しました"
        status_text.color = GREEN
        return True

    def selected_records(kind=None):
        return [
            record
            for record in records
            if record["grade"] == selected_grade
            and record["class_name"] == selected_class
            and record["subject_id"] == selected_subject
            and (kind is None or record["kind"] == kind)
        ]

    def open_form(record=None):
        nonlocal form_open, editing_id
        form_open = True
        editing_id = record["id"] if record else None
        render()

    def close_form():
        nonlocal form_open, editing_id
        form_open = False
        editing_id = None
        render()

    def save_record(event):
        nonlocal form_open, editing_id
        values = [field.value.strip() for field in fields]
        if not values[0]:
            status_text.value = "タイトルを入力してください。"
            status_text.color = ORANGE
            page.update()
            return
        kind = current_view if current_view != "overview" else "test"
        record = next((item for item in records if item["id"] == editing_id), None)
        if record:
            record.update(
                subject_id=selected_subject,
                grade=selected_grade,
                class_name=selected_class,
                kind=kind,
                title=values[0],
                date=values[1],
                detail=values[2],
            )
        else:
            records.insert(
                0,
                {
                    "id": str(uuid4()),
                    "subject_id": selected_subject,
                    "grade": selected_grade,
                    "class_name": selected_class,
                    "kind": kind,
                    "title": values[0],
                    "date": values[1],
                    "detail": values[2],
                    "done": False,
                },
            )
        if persist():
            form_open = False
            editing_id = None
        render()

    def delete_record(record_id):
        records[:] = [record for record in records if record["id"] != record_id]
        persist()
        render()

    def toggle_done(record_id):
        record = next((item for item in records if item["id"] == record_id), None)
        if record:
            record["done"] = not record["done"]
            persist()
            render()

    def choose_view(view):
        nonlocal current_view, form_open, editing_id
        current_view = view
        form_open = False
        editing_id = None
        render()

    def choose_subject(subject_id):
        nonlocal selected_subject, form_open, editing_id
        if any(item["id"] == subject_id for item in current_subjects()):
            selected_subject = subject_id
        form_open = False
        editing_id = None
        render()

    def choose_grade(grade):
        nonlocal selected_grade, selected_class, form_open, editing_id
        selected_grade = grade
        selected_class = CLASS_GROUPS[grade][0]
        ensure_selected_subject()
        form_open = False
        editing_id = None
        render()

    def choose_class(class_name):
        nonlocal selected_class, form_open, editing_id
        selected_class = class_name
        ensure_selected_subject()
        form_open = False
        editing_id = None
        render()

    def add_subject(event):
        if (selected_grade, selected_class) in CLASS_SUBJECTS:
            return
        name = subject_input.value.strip()
        if not name:
            status_text.value = "教科名を入力してください。"
            status_text.color = ORANGE
            page.update()
            return
        if any(subject["name"] == name for subject in subjects):
            status_text.value = "同じ名前の教科がすでにあります。"
            status_text.color = ORANGE
            page.update()
            return
        subject = {"id": str(uuid4()), "name": name}
        subjects.append(subject)
        if persist():
            subject_input.value = ""
            choose_subject(subject["id"])
        else:
            subjects.pop()

    subject_input = ft.TextField(
        hint_text="教科を追加",
        width=180,
        height=42,
        text_size=13,
        border_radius=8,
        border_color=LINE,
        on_submit=add_subject,
    )

    def text_label(value, size=13, color=INK, weight=None):
        return ft.Text(value, size=size, color=color, weight=weight)

    def record_card(record):
        kind_labels = {
            "test": "テスト範囲",
            "assignment": "提出物",
            "progress": "授業の進度",
        }
        done = record["done"]
        details = [
            ft.Row(
                [
                    ft.Container(
                        content=text_label(kind_labels[record["kind"]], 11, GREEN),
                        bgcolor=GREEN_LIGHT,
                        padding=ft.Padding.symmetric(horizontal=10, vertical=5),
                        border_radius=14,
                    ),
                    text_label(record["date"] or "日付未設定", 12, MUTED),
                ],
                spacing=10,
            ),
            text_label(
                record["title"],
                16,
                MUTED if done else INK,
                ft.FontWeight.W_600,
            ),
            text_label(record["detail"], 13, MUTED),
        ]
        actions = []
        if record["kind"] == "assignment":
            actions.append(
                ft.TextButton(
                    "提出済み" if done else "提出した",
                    icon=ft.Icons.CHECK_CIRCLE if done else ft.Icons.RADIO_BUTTON_UNCHECKED,
                    on_click=lambda event, item_id=record["id"]: toggle_done(item_id),
                )
            )
        actions.extend(
            [
                ft.IconButton(
                    icon=ft.Icons.EDIT_OUTLINED,
                    tooltip="編集",
                    on_click=lambda event, item=record: open_form(item),
                ),
                ft.IconButton(
                    icon=ft.Icons.DELETE_OUTLINE,
                    tooltip="削除",
                    on_click=lambda event, item_id=record["id"]: delete_record(item_id),
                ),
            ]
        )
        details.append(
            ft.Row(
                actions,
                alignment=ft.MainAxisAlignment.END,
                spacing=0,
            )
        )
        return ft.Container(
            content=ft.Column(details, spacing=8),
            padding=16,
            bgcolor="#FFFFFF",
            border=ft.Border.all(1, LINE),
            border_radius=12,
        )

    def section_header(title, count, kind):
        return ft.Row(
            [
                ft.Row(
                    [
                        text_label(title, 17, INK, ft.FontWeight.W_600),
                        text_label(f"{count}件", 12, MUTED),
                    ],
                    spacing=10,
                ),
                ft.TextButton(
                    "一覧を見る",
                    on_click=lambda event, view=kind: choose_view(view),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

    def render():
        nonlocal fields
        page.padding = 14 if (page.width or 900) < 600 else 24
        available_width = min(920, (page.width or 968) - page.padding * 2)

        grade_buttons = [
            ft.TextButton(
                grade,
                on_click=lambda event, value=grade: choose_grade(value),
                style=ft.ButtonStyle(
                    color=GREEN if grade == selected_grade else MUTED,
                    bgcolor=GREEN_LIGHT if grade == selected_grade else "#FFFFFF",
                    shape=ft.RoundedRectangleBorder(radius=18),
                    padding=ft.Padding.symmetric(horizontal=14, vertical=9),
                ),
            )
            for grade in CLASS_GROUPS
        ]
        class_buttons = [
            ft.TextButton(
                class_name,
                on_click=lambda event, value=class_name: choose_class(value),
                style=ft.ButtonStyle(
                    color=GREEN if class_name == selected_class else MUTED,
                    bgcolor=GREEN_LIGHT if class_name == selected_class else "#FFFFFF",
                    shape=ft.RoundedRectangleBorder(radius=18),
                    padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                ),
            )
            for class_name in CLASS_GROUPS[selected_grade]
        ]
        available_subjects = current_subjects()
        ensure_selected_subject()
        subject_buttons = [
            ft.TextButton(
                subject["name"],
                on_click=lambda event, subject_id=subject["id"]: choose_subject(subject_id),
                style=ft.ButtonStyle(
                    color=GREEN if subject["id"] == selected_subject else MUTED,
                    bgcolor=GREEN_LIGHT if subject["id"] == selected_subject else "#FFFFFF",
                    shape=ft.RoundedRectangleBorder(radius=18),
                    padding=ft.Padding.symmetric(horizontal=14, vertical=9),
                ),
            )
            for subject in available_subjects
        ]
        if (selected_grade, selected_class) not in CLASS_SUBJECTS:
            subject_buttons.extend(
                [
                    subject_input,
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        tooltip="教科を追加",
                        on_click=add_subject,
                        bgcolor=GREEN_LIGHT,
                        icon_color=GREEN,
                    ),
                ]
            )

        navigation = ft.Row(
            [
                ft.TextButton(
                    label,
                    on_click=lambda event, view=view: choose_view(view),
                    style=ft.ButtonStyle(
                        color=GREEN if current_view == view else MUTED,
                        bgcolor=GREEN_LIGHT if current_view == view else "transparent",
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                )
                for view, label in view_labels.items()
            ],
            spacing=4,
            scroll=ft.ScrollMode.AUTO,
        )

        body.controls = []
        if current_view == "overview":
            tests = selected_records("test")
            assignments = selected_records("assignment")
            progress = selected_records("progress")
            body.controls.extend(
                [
                    ft.Row(
                        [
                            summary_card("テスト", len(tests), "範囲・日程"),
                            summary_card(
                                "提出物",
                                sum(not item["done"] for item in assignments),
                                "未提出",
                            ),
                            summary_card("授業進度", len(progress), "更新"),
                        ],
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                    ),
                ]
            )
            for title, items, kind in (
                ("次のテスト", tests, "test"),
                ("提出物", assignments, "assignment"),
                ("最近の授業", progress, "progress"),
            ):
                body.controls.append(section_header(title, len(items), kind))
                body.controls.extend(
                    record_card(item) for item in sorted(items, key=lambda row: row["date"])[:2]
                )
                if not items:
                    body.controls.append(empty_state("まだ登録がありません。"))
        else:
            kind = current_view
            body.controls.append(
                ft.Row(
                    [
                        text_label(view_labels[kind], 22, INK, ft.FontWeight.W_600),
                        ft.Button(
                            "＋ 追加",
                            on_click=lambda event: open_form(),
                            bgcolor=GREEN,
                            color="#FFFFFF",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            )
            filtered = selected_records(kind)
            body.controls.extend(record_card(item) for item in filtered)
            if not filtered:
                body.controls.append(empty_state("まだ登録がありません。右上の「追加」から登録できます。"))

        if form_open and current_view != "overview":
            existing = next((item for item in records if item["id"] == editing_id), None)
            is_editing = existing is not None
            title_field = ft.TextField(
                label="タイトル",
                value=existing["title"] if existing else "",
                autofocus=True,
                border_radius=8,
            )
            date_field = ft.TextField(
                label="日付",
                hint_text="例: 2026-11-05",
                value=existing["date"] if existing else "",
                border_radius=8,
            )
            detail_field = ft.TextField(
                label="内容・範囲・次回予定",
                value=existing["detail"] if existing else "",
                multiline=True,
                min_lines=2,
                max_lines=4,
                border_radius=8,
            )
            fields = [title_field, date_field, detail_field]
            body.controls.insert(
                1,
                ft.Container(
                    content=ft.Column(
                        [
                            text_label(
                                "情報を編集" if is_editing else f"{view_labels[current_view]}を追加",
                                17,
                                INK,
                                ft.FontWeight.W_600,
                            ),
                            title_field,
                            date_field,
                            detail_field,
                            ft.Row(
                                [
                                    ft.TextButton("キャンセル", on_click=lambda event: close_form()),
                                    ft.Button(
                                        "保存",
                                        on_click=save_record,
                                        bgcolor=GREEN,
                                        color="#FFFFFF",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ],
                        spacing=12,
                    ),
                    padding=18,
                    bgcolor=GREEN_LIGHT,
                    border_radius=12,
                ),
            )
        else:
            fields = []

        header = ft.Column(
            [
                ft.Row(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    content=text_label("学", 14, "#FFFFFF", ft.FontWeight.BOLD),
                                    width=34,
                                    height=34,
                                    bgcolor=GREEN,
                                    border_radius=17,
                                    alignment=ft.Alignment.CENTER,
                                ),
                                ft.Column(
                                    [
                                        text_label("CLASS BOARD", 11, GREEN, ft.FontWeight.BOLD),
                                        text_label("クラスボード", 17, INK, ft.FontWeight.W_600),
                                    ],
                                    spacing=0,
                                ),
                            ],
                            spacing=10,
                        ),
                        text_label(date.today().strftime("%Y年%m月%d日"), 12, MUTED),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Column(
                    [
                        text_label(
                            "授業のこと、ここで共有。", 30, INK, ft.FontWeight.W_600
                        ),
                        text_label(
                            "学年・クラスを選んで、テスト範囲や提出物を確認できます。",
                            13,
                            MUTED,
                        ),
                    ],
                    spacing=5,
                ),
                text_label("学年", 12, MUTED, ft.FontWeight.W_600),
                ft.Row(
                    grade_buttons,
                    spacing=8,
                    wrap=True,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                text_label("クラス・コース", 12, MUTED, ft.FontWeight.W_600),
                ft.Row(
                    class_buttons,
                    spacing=6,
                    wrap=True,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                text_label("教科", 12, MUTED, ft.FontWeight.W_600),
                ft.Row(
                    subject_buttons,
                    spacing=8,
                    wrap=True,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                navigation,
                status_text,
            ],
            spacing=18,
        )
        page.controls.clear()
        page.add(
            ft.Container(
                content=ft.Column([header, body], spacing=22),
                width=available_width,
                padding=ft.Padding.only(top=10, bottom=32),
            )
        )
        page.update()

    def summary_card(label, value, caption):
        return ft.Container(
            content=ft.Column(
                [
                    text_label(label, 12, MUTED),
                    text_label(str(value), 26, GREEN, ft.FontWeight.W_600),
                    text_label(caption, 11, MUTED),
                ],
                spacing=4,
            ),
            padding=16,
            expand=True,
            bgcolor="#FFFFFF",
            border=ft.Border.all(1, LINE),
            border_radius=12,
        )

    def empty_state(message):
        return ft.Container(
            content=text_label(message, 13, MUTED),
            padding=18,
            bgcolor="#FFFFFF",
            border=ft.Border.all(1, LINE),
            border_radius=12,
        )

    page.on_resize = render
    render()


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
