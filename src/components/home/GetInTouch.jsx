import React, { useState, useContext } from "react";
import { Container, Form, Button, Alert } from "react-bootstrap";
import { LanguageContext } from "../../context/LanguageContext";

const GetInTouch = ({ heading, message, email }) => {
  const { language } = useContext(LanguageContext);
  const [formData, setFormData] = useState({ name: "", email: "", message: "" });
  const [status, setStatus] = useState({ type: "", msg: "" });
  const [loading, setLoading] = useState(false);

  const t = {
    it: {
      emailText: "Puoi mandarmi una mail a",
      orUseForm: "oppure usare direttamente il modulo qui sotto!",
      nameLabel: "Nome",
      namePlaceholder: "Inserisci il tuo nome",
      emailLabel: "Email",
      emailPlaceholder: "La tua email per essere ricontattato",
      messageLabel: "Messaggio",
      messagePlaceholder: "Scrivi qui la tua idea, proposta o un semplice saluto...",
      sending: "Invio in corso...",
      send: "Invia Messaggio",
      successMsg: "Messaggio inviato con successo!",
      errorMsg: "Si è verificato un errore.",
      networkError: "Errore di rete: Impossibile contattare il server. Riprova più tardi.",
    },
    en: {
      emailText: "You can email me at",
      orUseForm: "or use the form below directly!",
      nameLabel: "Name",
      namePlaceholder: "Enter your name",
      emailLabel: "Email",
      emailPlaceholder: "Your email to be contacted",
      messageLabel: "Message",
      messagePlaceholder: "Write here your idea, proposal, or a simple hello...",
      sending: "Sending...",
      send: "Send Message",
      successMsg: "Message sent successfully!",
      errorMsg: "An error occurred.",
      networkError: "Network error: Unable to contact the server. Please try again later.",
    }
  };

  const currT = t[language] || t.it;

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setStatus({ type: "", msg: "" });

    try {
      // Effettua la chiamata API verso il nuovo server in produzione
      const response = await fetch("https://simonkolaaa.pythonanywhere.com/api/contact", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        setStatus({ type: "success", msg: data.success || currT.successMsg });
        // Svuota i campi del form dopo un successo
        setFormData({ name: "", email: "", message: "" });
      } else {
        setStatus({ type: "danger", msg: data.error || currT.errorMsg });
      }
    } catch (error) {
      setStatus({ type: "danger", msg: currT.networkError });
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container id="contact" className="pb-5">
      <h2 className="display-4 pb-3 text-center">{heading}</h2>
      <p className="lead text-center pb-3">
        {message}
        <br />
        {currT.emailText} <a className="text-decoration-none" href={`mailto:${email}`}>{email}</a> {currT.orUseForm}
      </p>
      
      <div className="row justify-content-center">
        <div className="col-md-8 col-lg-6">
          {status.msg && <Alert variant={status.type} className="text-center shadow-sm">{status.msg}</Alert>}
          
          <Form onSubmit={handleSubmit} className="shadow-lg p-4 bg-white rounded">
            <Form.Group className="mb-3" controlId="formName">
              <Form.Label className="fw-bold">{currT.nameLabel}</Form.Label>
              <Form.Control 
                type="text" 
                placeholder={currT.namePlaceholder}
                name="name"
                value={formData.name}
                onChange={handleChange}
                required 
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formEmail">
              <Form.Label className="fw-bold">{currT.emailLabel}</Form.Label>
              <Form.Control 
                type="email" 
                placeholder={currT.emailPlaceholder}
                name="email"
                value={formData.email}
                onChange={handleChange}
                required 
              />
            </Form.Group>

            <Form.Group className="mb-4" controlId="formMessage">
              <Form.Label className="fw-bold">{currT.messageLabel}</Form.Label>
              <Form.Control 
                as="textarea" 
                rows={5} 
                placeholder={currT.messagePlaceholder}
                name="message"
                value={formData.message}
                onChange={handleChange}
                required 
              />
            </Form.Group>

            <div className="d-grid">
              <Button variant="primary" type="submit" size="lg" disabled={loading}>
                {loading ? currT.sending : currT.send}
              </Button>
            </div>
          </Form>

        </div>
      </div>
    </Container>
  );
};

export default GetInTouch;
