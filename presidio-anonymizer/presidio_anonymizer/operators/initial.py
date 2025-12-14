from presidio_anonymizer.operators.operator import Operator


class Initial(Operator):
    def operator_name(self) -> str:
        return "initial"

    def operator_type(self):
        # Late import to avoid circular dependency
        from presidio_anonymizer.operators import OperatorType

        return OperatorType.Anonymize

    def validate(self, params: dict = None):
        return

    def operate(self, text: str, params: dict = None) -> str:
        return "<REDACTED>"
