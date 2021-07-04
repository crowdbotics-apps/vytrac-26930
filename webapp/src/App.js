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
            <Col className="login-background-image-gradient" xs={8}>
              <img className="login-background-image" src={loginBackground}></img>
              <div className="login-user-thumb"></div>
              <div className="logos-container">
                <img className="login-logo-top" src={poweredBy}></img>
                <img className="login-logo-bottom" src={vytracWhite}></img>
              </div>              
            </Col>
            <Col className="login-form" xs={4}>
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
              <Button>LOGIN</Button>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default App;