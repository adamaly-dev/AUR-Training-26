pragma ComponentBehavior: Bound
import QtQuick
import QtQuick.Shapes

Rectangle{
    property int clockData
    property int sec: clockData % 60
    property int min: (clockData / 60) % 60
    property int hour: clockData / 3600

    id: root
    width: 300
    height: 300
    color: palette.window

    Rectangle{
        id: clock
        width: (parent.height > parent.width ? parent.width : parent.height)
        height: width
        radius: width / 2
        border.width: 6
        border.color: '#aaa'
        anchors.centerIn: root

        Repeater{
            model: 60

            delegate:Item{
                id: tickContainer

                required property int index

                anchors.bottom: clock.verticalCenter
                anchors.topMargin: 16
                anchors.top: clock.top
                anchors.horizontalCenter: parent.horizontalCenter

                rotation: index * 6
                transformOrigin: Item.Bottom

                Rectangle{
                    width: (parent.index%5 ? 2 : 5)
                    height: (parent.index%5 ? 10 : 12)
                    color: 'black'
                    anchors.top: parent.top
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Text{
                    color: 'black'
                    text: (parent.index%5 ? '' : (parent.index ? parent.index/5 : 12))
                    font.pixelSize: 16
                    font.bold: true

                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.top: parent.top
                    anchors.topMargin: 16
                    rotation: -parent.rotation
                }
            }

        }

        Shape{
            id: hour
            width: parent.width * 0.04
            anchors.topMargin: parent.height * 0.15
            anchors.top: parent.top
            anchors.bottom: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            rotation: root.hour * 30 + root.min * 30 / 60
            transformOrigin: Item.Bottom

            ShapePath{
                strokeColor: 'black'
                strokeWidth: 1
                fillColor: 'black'

                startX: 0
                startY: hour.height
                
                PathLine{x: hour.width; y: hour.height}
                PathLine{x: hour.width / 2; y: 0}
                PathLine{x: 0; y: hour.height}
            }
        }

        Shape{
            id: min
            width: parent.width * 0.025
            anchors.topMargin: parent.height * 0.1
            anchors.top: parent.top
            anchors.bottom: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            rotation: root.min * 6 + root.sec * 30 / 60
            transformOrigin: Item.Bottom

            ShapePath{
                strokeColor: 'black'
                strokeWidth: 1
                fillColor: 'black'

                startX: 0
                startY: min.height
                
                PathLine{x: min.width; y: min.height}
                PathLine{x: min.width / 2; y: 0}
                PathLine{x: 0; y: min.height}
            }
        }

        Shape{
            id: sec
            anchors.topMargin: parent.height * 0.05
            anchors.top: parent.top
            anchors.bottom: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            rotation: root.sec * 6
            transformOrigin: Item.Bottom

            ShapePath{
                strokeColor: 'red'
                strokeWidth: 3
                fillColor: 'red'

                startX: 0
                startY: sec.height
                
                PathLine{x: 0; y: 0}
                PathLine{x: 0; y: sec.height}
            }
        }
    }
}
