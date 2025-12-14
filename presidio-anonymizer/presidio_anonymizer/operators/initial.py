from presidio_anonymizer.operators.operator import Operator


class Initial(Operator):
    def operator_name(self) -> str:
        return "initial"

    def operator_type(self):
        from presidio_anonymizer.operators import OperatorType
        return OperatorType.Anonymize

    def validate(self, params: dict = None):
        return

    def operate(self, text: str, params: dict = None) -> str:
        # Split on whitespace
        words = text.split()

        # Take first character of each word, uppercase it, add "."
        initials = [word[0].upper() + "." for word in words if word]

        # Join with spaces
        return " ".join(initials)
