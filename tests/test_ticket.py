import pytest
import io
import sys
from zendesk_ticket_viewer.ticket import ZendeskTicket
from tests.fixtures import example_zendeskTicket


@pytest.fixture()
def zendesk_ticket():
    testTicket = ZendeskTicket(example_zendeskTicket.data())
    return testTicket


@pytest.mark.unitTest
def test_zendesk_ticket_init(zendesk_ticket):
    assert(zendesk_ticket.id == 1)
    assert (zendesk_ticket.subject == 'Sample ticket: Meet the ticket')
    assert (zendesk_ticket.description == 'Hi this is a test ticket\n')
    assert (zendesk_ticket.updated_at == '2017-11-18T07:20:59Z')


@pytest.mark.unitTest
def test_zendesk_ticket_init_fail(zendesk_ticket):
    with pytest.raises(ValueError):
        zendesk_ticket = {'from': {}, 'rel': None, 'to': {}}
        ZendeskTicket(zendesk_ticket)


@pytest.mark.unitTest
def test_zendesk_ticket_str(zendesk_ticket):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print(zendesk_ticket)
    sys.stdout = sys.__stdout__

    assert '1' in capturedOutput.getvalue()
    assert 'Sample ticket: Meet the ticket' in capturedOutput.getvalue()
    assert 'Hi this is a test ticket\n' in capturedOutput.getvalue()
    assert '2017-11-18T07:20:59Z' in capturedOutput.getvalue()



