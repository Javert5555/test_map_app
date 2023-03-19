// import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import { MapContainer, TileLayer, useMap } from 'react-leaflet'

function MyComponent() {
    const map = useMap()
    map.attributionControl.setPrefix('')
    // map.setCenter([50.5, 30.5])
    // map.attributionControl.setZoom(false)
    // console.log('map center:', map.getCenter())
    return null
  }
  

function Model() {
    return (
        // <MapContainer 
        // style={{
        //     margin: 0,
        //     overflow: 'hidden',
        //     position: 'fixed',
        //     width: '500px',
        //     height: '500px'
        // }}
        // center={[51.505, -0.09]}
        // zoom={13}
        
        // scrollWheelZoom={false}>
        // <TileLayer
        //     attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        //     url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        // />
        // <Marker position={[51.505, -0.09]}>
        //     <Popup>
        //     A pretty CSS3 popup. <br /> Easily customizable.
        //     </Popup>
        // </Marker>
        // </MapContainer>
        <MapContainer
        style={{
            margin: 0,
            overflow: 'hidden',
            position: 'fixed',
            width: '500px',
            height: '500px'
        }}
        center={[51.505, -0.09]}
        zoom={13}
        >
            <TileLayer
                url="http://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}@2x.png"
            />
            <MyComponent>
            </MyComponent>
        </MapContainer>
    )
}

export default Model;