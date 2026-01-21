import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';


const customIcon = new L.Icon({
  iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
  iconRetinaUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
  iconSize: [25, 41],          // 圖示大小
  iconAnchor: [12, 41],        // 圖示錨點（尖端位置）
  popupAnchor: [1, -34],       // Popup 出現位置
  shadowSize: [41, 41],
});

interface MapProps {
  lat: number | string;
  lng: number | string;
  address?: string;
  zoom?: number;
  height?: string;
  mapId?: string;
}


export default function Map({
  lat,
  lng,
  address = 'address',
  zoom = 15,
  height = '400px',
  mapId = 'map',
  ...rest
}: MapProps) {
  const latitude = Number(lat);
  const longitude = Number(lng);

  if (isNaN(latitude) || isNaN(longitude)) {
    return (
      <div className="w-full overflow-hidden rounded shadow-md" style={{ height }}>
        Invalid latitude and longitude data
      </div>
    );
  }

  const position: [number, number] = [latitude, longitude];

  return (
    <div className="w-full overflow-hidden rounded shadow-md" style={{ height }} id={mapId}>
      <MapContainer
        center={position}
        zoom={zoom}
        scrollWheelZoom={false}
        className="h-full"
        {...rest}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <Marker
          position={position}
          icon={customIcon}
        >
          <Popup>{address}</Popup>
        </Marker>
      </MapContainer>
    </div>
  );
}