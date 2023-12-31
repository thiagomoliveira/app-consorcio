from utils.notification_validations import *
from utils.type_conversion import convert_date
from sqlalchemy import Column, Integer, String, Date
from database.database_config import Base

class Notification(Base):
    __tablename__ = 'notificações'

    id = Column(Integer, primary_key=True)
    _group = Column(String, name='Grupo')
    _quota = Column(String, name='Cota')
    _send_date = Column(Date, name='DataDeEnvio')
    _return_date = Column(Date, name='DataDeRetorno')
    _return_type = Column(String, name='TipoDoRetorno')
    _office = Column(String, name='Escritório')
    _state = Column(String, name='UF')
    _registry_office = Column(String, name='Cartório')
    _name = Column(String, name='Nome')
    _contract = Column(String, name='Contrato')
    _justification = Column(String, name='Justificativa')

    def __init__(self, group, quota, send_date, return_date, return_type, office, state, registry_office, name, contract, justification):
        self.group = group
        self.quota = quota
        self.send_date = send_date
        self.return_date = return_date
        self.return_type = return_type
        self.office = office
        self.state = state
        self.registry_office = registry_office
        self.name = name
        self.contract = contract
        self.justification = justification

        # Perform validation
        self.is_valid, self.errors = validate_notification_data(
            group, quota, send_date, return_date, return_type, office, state, registry_office, name, contract, justification)
        
        # Convert the dates if the notification is valid
        if self.is_valid:
            self._send_date = convert_date(send_date)
            self._return_date = convert_date(return_date)
        else:
            # Set attributes for invalid notifications
            self._send_date = send_date
            self._return_date = return_date

    # Group
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = validate_numeric(value, "group")

    # Quota
    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, value):
        self._quota = validate_numeric(value, "quota")

    # Send Date
    @property
    def send_date(self):
        return self._send_date

    @send_date.setter
    def send_date(self, value):
        self._send_date = validate_date(value)

    # Return Date
    @property
    def return_date(self):
        return self._return_date

    @return_date.setter
    def return_date(self, value):
        self._return_date = validate_date(value)

    # Return Type
    @property
    def return_type(self):
        return self._return_type

    @return_type.setter
    def return_type(self, value):
        self._return_type = validate_not_empty(value, "Return Type")

    # Office
    @property
    def office(self):
        return self._office

    @office.setter
    def office(self, value):
        self._office = validate_not_empty(value, "Office")

    # State
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = validate_state(value)

    # Registry Office
    @property
    def registry_office(self):
        return self._registry_office

    @registry_office.setter
    def registry_office(self, value):
        self._registry_office = validate_not_empty(value, "Registry Office")

    # Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = validate_not_empty(value, "Name")

    # Contract
    @property
    def contract(self):
        return self._contract

    @contract.setter
    def contract(self, value):
        self._contract = validate_numeric(value, "contract")

    # Justification
    @property
    def justification(self):
        return self._justification

    @justification.setter
    def justification(self, value):
        self._justification = validate_not_empty(value, "Justification")

    def revalidate(self):
        self.is_valid, self.errors = validate_notification_data(
            self.group, self.quota, self.send_date, self.return_date, self.return_type,
            self.office, self.state, self.registry_office, self.name, self.contract, self.justification
        )

        if self.is_valid:
            self.send_date = convert_date(self.send_date)
            self.return_date = convert_date(self.return_date)
            return {"status": "success", "message": "Notification successfully validated."}
        else:
            return {"status": "error", "message": "Validation errors found.", "errors": self.errors}

    def __eq__(self, other):
        if not isinstance(other, Notification):
            return False
        return (self.group, self.quota) == (other.group, other.quota)

    def __hash__(self):
        return hash((self.group, self.quota))

    def __str__(self):
        return (f"Notification(group={self.group}, quota={self.quota}, send_date={self.send_date}, "
                f"return_date={self.return_date}, return_type={self.return_type}, office={self.office}, "
                f"state={self.state}, registry_office={self.registry_office}, name={self.name}, "
                f"contract={self.contract}, justification={self.justification}, is_valid={self.is_valid}, errors={self.errors})")
