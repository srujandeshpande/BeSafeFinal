import React, { Component } from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import './Home.css';
import logo from './logo.png';


class NavBar extends Component {

    constructor(props) {
        super(props);
        this.state = {currentPage: 1};
        this._pageScroller = null;
    }

    goToPage = (eventKey) => {
        this._pageScroller.goToPage(eventKey);
    };

    render() {
        return (
            <Navbar expand="lg" fixed="top" className="navbar">
                <Navbar.Brand onSelect={this.goToPage(0)}><img src={logo} className="nav-logo"/></Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="ml-auto">
                        <Nav.Link href="#home">Home</Nav.Link>
                        <Nav.Link href="#link">Link</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        );
    }
}

export default NavBar;