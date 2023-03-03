class Particulars:
    index_number: str
    first_name: str
    middle_name: str
    last_name: str
    sex: str
    center_number: str
    center_name: str
    exam_id: int

    def __init__(self, index_number: str, first_name: str, middle_name: str, last_name: str, sex: str, center_number: str, center_name: str, exam_id: int) -> None:
        self.index_number = index_number
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.sex = sex
        self.center_number = center_number
        self.center_name = center_name
        self.exam_id = exam_id


class Status:
    code: int
    message: str

    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message


class NectaResponse:
    particulars: Particulars
    status: Status

    def __init__(self, particulars: Particulars, status: Status) -> None:
        self.particulars = particulars
        self.status = status
