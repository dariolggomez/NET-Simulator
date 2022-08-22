class Style():

    style_bt_standard = (
    """
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        border-right: 5px solid rgb(44, 49, 60);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton:hover {
        background-color: rgb(33, 37, 43);
        border-left: 28px solid rgb(33, 37, 43);
    }
    QPushButton:pressed {
        background-color: rgb(85, 170, 255);
        border-left: 28px solid rgb(85, 170, 255);
    }
    """
    )

    style_table_users = (
     """
    QTableWidget {	
	    background-color: rgb(39, 44, 54);
	    padding: 10px;
	    border-radius: 5px;
	    gridline-color: rgb(44, 49, 60);
	    border-bottom: 1px solid rgb(44, 49, 60);
    }
    QTableWidget::item{
	    border-color: rgb(44, 49, 60);
	    padding-left: 5px;
	    padding-right: 5px;
	    gridline-color: rgb(44, 49, 60);
    }
    QTableWidget::item:selected{
	    background-color: rgb(85, 170, 255);
    }
    QScrollBar:horizontal {
        border: none;
        background: rgb(52, 59, 72);
        height: 14px;
        margin: 0px 21px 0 21px;
	    border-radius: 0px;
    }
    QScrollBar:vertical {
	    border: none;
        background: rgb(52, 59, 72);
        width: 14px;
        margin: 21px 0 21px 0;
	    border-radius: 0px;
    }
    QHeaderView::section{
	    Background-color: rgb(39, 44, 54);
	    max-width: 30px;
	    border: 1px solid rgb(44, 49, 60);
	    border-style: none;
        border-bottom: 1px solid rgb(44, 49, 60);
        border-right: 1px solid rgb(44, 49, 60);
    }
    QTableWidget::horizontalHeader {	
	    background-color: rgb(81, 255, 0);
    }
    QHeaderView::section:horizontal {
        border: 1px solid rgb(32, 34, 42);
	    background-color: rgb(27, 29, 35);
	    padding: 3px;
	    border-top-left-radius: 7px;
        border-top-right-radius: 7px;
    }
    QHeaderView::section:vertical {
        border: 1px solid rgb(44, 49, 60);
    }
    """
    )
    
