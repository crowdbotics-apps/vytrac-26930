import React, { Component, View } from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import './App.css';

import loginBackground from './assets/images/login_background.png';
import poweredBy from './assets/images/powered_by.png';
import vytracWhite from './assets/images/vytrac_white.png';

class App extends Component {
  render() {
    return (
      <div className="login-background"> 
        <Container className="login-container">
          <Row className="login-row">
            <Col className="login-background-image-gradient" xs={7}>
              <img className="login-background-image" src={loginBackground}></img>
              <div className="login-user-thumb"></div>
              <div className="logos-container">
                <img className="login-logo-top" src={poweredBy}></img>
                <img className="login-logo-bottom" src={vytracWhite}></img>
              </div>              
            </Col>
            <Col className="login-form" xs={5}>
              <Row className="vertical-container">
                <Col style={{padding: 0, margin: 0}}>
                  <div className="green-line"></div>
                </Col>
                <Col style={{padding: 0, margin: 0}}>
                  <div className="grey-line"></div>
                </Col>
              </Row>  
              <p className="text-left">Welcome to <span className="bold-blue">VyTrac</span></p>

              <p className="text-left smaller-text">Lorem ipsum dolor sit amet, cons cdipiscing elit. Duis non turpis nec nunc </p>

              <p className="grey-text username-label">Username, Email or Phone number</p>
              <input className="text-field" type="text" name="username" />
              <input className="text-field" type="text" name="password" />

              <Row className="vertical-container remember-me">
                <Col style={{padding: 0, margin: 0}}  xs={1}>
                  <div className="greycheck" />
                </Col>
                <Col style={{padding: 0, margin: 0}}>
                  <span className="grey-text">&nbsp;&nbsp;&nbsp;&nbsp;Remember me</span>
                </Col>
              </Row>  

              <div className="login-bottom-buttons-container">
                <Button style={{marginRight: 50}} variant="light">FORGOT PASSWORD</Button>
                <Button>LOGIN</Button>
              </div>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default App;