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
        words = text.split()
        result = []

        for word in words:
            prefix = ""
            initial_char = None

            for ch in word:
                if ch.isalnum():
                    initial_char = ch.upper()
                    break
                else:
                    prefix += ch

            if initial_char:
                result.append(f"{prefix}{initial_char}.")

        return " ".join(result)
