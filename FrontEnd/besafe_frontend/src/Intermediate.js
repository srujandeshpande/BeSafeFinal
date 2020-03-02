import React, { Component } from 'react';
import ReactPageScroller from 'react-page-scroller';
import './Home.css';
import { Nav, Container, Row, Col, Button, Pager, Pagination } from 'react-bootstrap';
import logo from './logo.png';
import { Link } from 'react-router-dom';
import Navbar from './Navbar'
import SignInSide from './SignInSide'

function Comp(){
    return(
        <div>
            <Row>
                <Col>
                <Link href = "http://localhost:3000/Select/map"
              className="btn btn-primary"
              type="submit"
              onClick= "" 
              fullWidth
              variant="contained"
              color="primary"
            >
              AUSTIN
            </Link>
                </Col>
                <Col>
                <Link href = "http://localhost:3000/Select/map"
              className="btn btn-primary"
              type="submit"
              onClick= "" 
              fullWidth
              variant="contained"
              color="primary"
            >
              TORONTO
            </Link>
                </Col>
            </Row>
        </div>
    );
} 

class Intermediate extends Component {
    render() {
        return (
            <Comp/>
        );
    }
}

export default Intermediate;
