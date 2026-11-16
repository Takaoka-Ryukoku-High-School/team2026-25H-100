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
    ("2年生", "L&Sコース"): [
        ("2-ls-sports-synthesis", "スポーツ総合"),
        ("2-ls-welfare-basics", "福祉基礎"),
        ("2-ls-sports-science", "スポーツサイエンス"),
    ],
    ("2年生", "デジタルコース"): [
        ("2-digital-biz", "Biz"),
        ("2-digital-tech", "Tech"),
        ("2-digital-tech-ad", "テクアド"),
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
SECOND_GRADE_ADDITIONAL_SUBJECTS = [
    ("music", "音楽"),
    ("art", "美術"),
    ("calligraphy", "書道"),
]


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
        "notifications": [],
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
    notifications = data.get("notifications")
    if not isinstance(subjects, list) or not isinstance(records, list):
        raise ValueError("保存データに科目または共有情報がありません。")
    if notifications is None:
        notifications = []
        data["notifications"] = notifications
    if not isinstance(notifications, list):
        raise ValueError("保存データの通知情報を読み込めません。")
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
    if any(
        not isinstance(notification, dict)
        or not isinstance(notification.get("id"), str)
        or not isinstance(notification.get("subject_id"), str)
        or not isinstance(notification.get("title"), str)
        or not isinstance(notification.get("date"), str)
        or not isinstance(notification.get("detail"), str)
        or not isinstance(notification.get("read"), bool)
        for notification in notifications
    ):
        raise ValueError("保存データの通知情報を読み込めません。")
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
    for notification in notifications:
        if "grade" not in notification:
            notification["grade"] = "1年生"
            migrated = True
        if "class_name" not in notification:
            notification["class_name"] = "1組"
            migrated = True
        if not isinstance(notification["grade"], str) or not isinstance(
            notification["class_name"], str
        ):
            raise ValueError("保存データの通知の学年・クラス情報を読み込めません。")
        source_record = next(
            (record for record in records if record["id"] == notification.get("source_id")),
            None,
        )
        if source_record and source_record["kind"] == "assignment" and notification.get("event_type") == "updated":
            subject_name = next(
                (subject["name"] for subject in subjects if subject["id"] == source_record["subject_id"]),
                "教科",
            )
            updated_title = f"{subject_name}の提出物が更新されました: {source_record['title']}"
            if notification["title"] != updated_title:
                notification["title"] = updated_title
                migrated = True
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
    notifications = data["notifications"]
    selected_grade = "1年生"
    selected_class = CLASS_GROUPS[selected_grade][0]
    selected_subject = subjects[0]["id"] if subjects else ""
    current_view = "assignment"
    form_open = False
    editing_id = None
    fields = []
    status_text = ft.Text("", size=12, color=ORANGE)
    body = ft.Column(spacing=16)

    view_labels = {
        "assignment": "提出物",
        "progress": "授業進行度",
        "test": "テスト範囲",
    }

    def current_subjects():
        class_key = (selected_grade, selected_class)
        scoped_names = CLASS_SUBJECTS.get(class_key)
        scoped_subject_ids = {
            subject_id
            for configured_subjects in CLASS_SUBJECTS.values()
            for subject_id, _ in configured_subjects
        }
        scoped_subject_ids.update(
            f"2-{number}-{subject_id}"
            for number in range(1, 8)
            for subject_id, _ in SECOND_GRADE_ADDITIONAL_SUBJECTS
        )
        if scoped_names is None:
            available_subjects = [
                subject for subject in subjects if subject["id"] not in scoped_subject_ids
            ]
            subject_names = []
        else:
            available_subjects = []
            subject_names = list(scoped_names)

        if selected_grade == "2年生" and selected_class in {
            f"{number}組" for number in range(1, 8)
        }:
            class_number = selected_class.removesuffix("組")
            subject_names.extend(
                (f"2-{class_number}-{subject_id}", name)
                for subject_id, name in SECOND_GRADE_ADDITIONAL_SUBJECTS
            )

        for subject_id, name in subject_names:
            subject = next(
                (item for item in subjects if item["id"] == subject_id), None
            )
            if subject is None:
                subject = {"id": subject_id, "name": name}
                subjects.append(subject)
            available_subjects.append(subject)
        return available_subjects

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

    def selected_notifications():
        return [
            item
            for item in notifications
            if item["grade"] == selected_grade
            and item["class_name"] == selected_class
        ]

    def notification_for_record(record, event_type):
        if event_type == "deadline":
            title = f"提出期限が近づいています: {record['title']}"
            detail = f"{record['date']} に提出予定です。忘れずに確認してください。"
        elif event_type == "status_changed":
            title = f"提出物の状態が変更されました: {record['title']}"
            detail = f"現在の状態: {'提出済み' if record['done'] else '未提出'}"
        elif record["kind"] == "assignment":
            subject_name = next(
                (
                    subject["name"]
                    for subject in subjects
                    if subject["id"] == record["subject_id"]
                ),
                "教科",
            )
            title = f"{subject_name}の提出物が更新されました: {record['title']}"
            detail = record["detail"]
        else:
            title = f"{view_labels.get(record['kind'], '項目')}が更新されました: {record['title']}"
            detail = record["detail"]
        return {
            "id": str(uuid4()),
            "subject_id": record["subject_id"],
            "grade": record["grade"],
            "class_name": record["class_name"],
            "title": title,
            "date": record["date"],
            "detail": detail,
            "read": False,
            "source_id": record["id"],
            "event_type": event_type,
        }

    def add_notification(record, event_type):
        if any(
            item.get("source_id") == record["id"] and item.get("event_type") == event_type
            for item in notifications
        ):
            return
        notifications.insert(0, notification_for_record(record, event_type))

    def sync_notifications():
        seen = {
            (item.get("source_id"), item.get("event_type"))
            for item in notifications
            if item.get("source_id") is not None and item.get("event_type") is not None
        }
        for record in records:
            if record["kind"] != "assignment" or record["done"]:
                continue
            try:
                due_date = date.fromisoformat(record["date"])
            except ValueError:
                continue
            days_left = (due_date - date.today()).days
            key = (record["id"], "deadline")
            if 0 <= days_left <= 3 and key not in seen:
                notifications.insert(0, notification_for_record(record, "deadline"))
                seen.add(key)

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
        kind = current_view
        record = next((item for item in records if item["id"] == editing_id), None)
        if record:
            existing_title = record["title"]
            existing_detail = record["detail"]
            existing_date = record["date"]
            record.update(
                subject_id=selected_subject,
                grade=selected_grade,
                class_name=selected_class,
                kind=kind,
                title=values[0],
                date=values[1],
                detail=values[2],
            )
            if (
                existing_title != values[0]
                or existing_detail != values[2]
                or existing_date != values[1]
            ):
                add_notification(record, "updated")
        else:
            record = {
                "id": str(uuid4()),
                "subject_id": selected_subject,
                "grade": selected_grade,
                "class_name": selected_class,
                "kind": kind,
                "title": values[0],
                "date": values[1],
                "detail": values[2],
                "done": False,
            }
            records.insert(0, record)
            add_notification(record, "updated")
        if persist():
            form_open = False
            editing_id = None
            sync_notifications()
        render()

    def delete_record(record_id):
        records[:] = [record for record in records if record["id"] != record_id]
        notifications[:] = [
            notification
            for notification in notifications
            if notification.get("source_id") != record_id
        ]
        persist()
        render()

    def toggle_done(record_id):
        record = next((item for item in records if item["id"] == record_id), None)
        if record:
            before = record["done"]
            record["done"] = not record["done"]
            if before != record["done"]:
                add_notification(record, "status_changed")
            persist()
            sync_notifications()
            render()

    def mark_notification_read(notification_id):
        notification = next((item for item in notifications if item["id"] == notification_id), None)
        if notification and not notification["read"]:
            notification["read"] = True
            persist()
            render()

    def open_notification_item(notification_id):
        nonlocal selected_grade, selected_class, selected_subject
        nonlocal current_view, form_open, editing_id
        notification = next(
            (item for item in notifications if item["id"] == notification_id),
            None,
        )
        record = next(
            (
                item
                for item in records
                if notification and item["id"] == notification.get("source_id")
            ),
            None,
        )
        if record is None:
            status_text.value = "通知に関連する項目が見つかりません。"
            status_text.color = ORANGE
            page.update()
            return
        selected_grade = record["grade"]
        selected_class = record["class_name"]
        selected_subject = record["subject_id"]
        current_view = record["kind"]
        form_open = False
        editing_id = None
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

    def notification_card(notification):
        is_read = notification["read"]
        has_source = any(
            record["id"] == notification.get("source_id") for record in records
        )
        metadata = ft.Row(
            [
                text_label(notification["date"] or "日付未設定", 12, MUTED),
                text_label("確認済み" if is_read else "未確認", 11, GREEN if is_read else ORANGE),
            ],
            spacing=10,
        )
        actions = []
        if has_source:
            actions.append(
                ft.TextButton(
                    "項目を開く",
                    icon=ft.Icons.OPEN_IN_NEW,
                    on_click=lambda event, item_id=notification["id"]: open_notification_item(item_id),
                )
            )
        if not is_read:
            actions.append(
                ft.TextButton(
                    "確認",
                    icon=ft.Icons.CHECK_CIRCLE_OUTLINE,
                    on_click=lambda event, item_id=notification["id"]: mark_notification_read(item_id),
                )
            )
        return ft.Container(
            content=ft.Column(
                [
                    metadata,
                    text_label(notification["title"], 15, INK, ft.FontWeight.W_600),
                    text_label(notification["detail"], 13, MUTED),
                    ft.Row(actions, alignment=ft.MainAxisAlignment.END) if actions else ft.Container(),
                ],
                spacing=8,
            ),
            padding=16,
            bgcolor="#FFFFFF" if not is_read else "#F7F7F5",
            border=ft.Border.all(1, LINE),
            border_radius=12,
        )

    def record_card(record):
        kind_labels = {
            "test": "テスト範囲",
            "assignment": "提出物",
            "progress": "授業進行度",
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

    def render():
        nonlocal fields
        sync_notifications()
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

        unsubmitted_count = sum(
            1
            for record in records
            if record["grade"] == selected_grade
            and record["class_name"] == selected_class
            and record["kind"] == "assignment"
            and not record["done"]
        )
        navigation_items = [
            (
                view,
                f"{label} ({unsubmitted_count})"
                if view == "assignment" and unsubmitted_count
                else label,
            )
            for view, label in view_labels.items()
        ] + [("notifications", "過去の通知")]
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
                for view, label in navigation_items
            ],
            spacing=4,
            scroll=ft.ScrollMode.AUTO,
        )

        body.controls = []
        kind = current_view
        if kind == "notifications":
            body.controls.append(
                text_label("過去の通知", 22, INK, ft.FontWeight.W_600)
            )
            filtered = selected_notifications()
            body.controls.extend(notification_card(item) for item in filtered)
            if not filtered:
                body.controls.append(empty_state("このクラスの通知はまだありません。"))
        else:
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

        if form_open:
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

        unread_notifications = [
            item
            for item in notifications
            if item["grade"] == selected_grade
            and item["class_name"] == selected_class
            and not item["read"]
        ]
        notification_badge = ft.Container(
            content=text_label(f"通知 {len(unread_notifications)}件", 11, GREEN),
            bgcolor=GREEN_LIGHT,
            padding=ft.Padding.symmetric(horizontal=10, vertical=5),
            border_radius=12,
        )
        notification_feed = []
        for notification in unread_notifications[:3]:
            notification_actions = []
            if any(
                record["id"] == notification.get("source_id") for record in records
            ):
                notification_actions.append(
                    ft.TextButton(
                        "項目を開く",
                        on_click=lambda event, item_id=notification["id"]: open_notification_item(item_id),
                    )
                )
            notification_actions.append(
                ft.TextButton(
                    "確認",
                    on_click=lambda event, item_id=notification["id"]: mark_notification_read(item_id),
                )
            )
            notification_feed.append(
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text(notification["title"], size=12, color=INK, weight=ft.FontWeight.W_600),
                                ft.Text(notification["detail"], size=11, color=MUTED),
                            ],
                            spacing=4,
                            expand=True,
                        ),
                        ft.Row(notification_actions, spacing=0),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        notification_panel = ft.Container(
            content=ft.Column(
                [
                    text_label("最新の通知", 12, MUTED, ft.FontWeight.W_600),
                    *notification_feed,
                ] if notification_feed else [text_label("現在のクラスでは通知はありません。", 12, MUTED)],
                spacing=6,
            ),
            padding=14,
            bgcolor="#FFFFFF",
            border=ft.Border.all(1, LINE),
            border_radius=12,
        ) if unread_notifications else ft.Container()
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
                        ft.Row(
                            [
                                notification_badge,
                                text_label(date.today().strftime("%Y年%m月%d日"), 12, MUTED),
                            ],
                            spacing=12,
                        ),
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
                notification_panel,
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
