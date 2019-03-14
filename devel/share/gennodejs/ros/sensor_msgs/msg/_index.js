
"use strict";

let LaserEcho = require('./LaserEcho.js');
let MagneticField = require('./MagneticField.js');
let CameraInfo = require('./CameraInfo.js');
let TimeReference = require('./TimeReference.js');
let Temperature = require('./Temperature.js');
let PointField = require('./PointField.js');
let Range = require('./Range.js');
let MultiDOFJointState = require('./MultiDOFJointState.js');
let Joy = require('./Joy.js');
let RegionOfInterest = require('./RegionOfInterest.js');
let Imu = require('./Imu.js');
let NavSatStatus = require('./NavSatStatus.js');
let JointState = require('./JointState.js');
let JoyFeedbackArray = require('./JoyFeedbackArray.js');
let FluidPressure = require('./FluidPressure.js');
let ChannelFloat32 = require('./ChannelFloat32.js');
let JoyFeedback = require('./JoyFeedback.js');
let Image = require('./Image.js');
let RelativeHumidity = require('./RelativeHumidity.js');
let LaserScan = require('./LaserScan.js');
let Illuminance = require('./Illuminance.js');
let CompressedImage = require('./CompressedImage.js');
let MultiEchoLaserScan = require('./MultiEchoLaserScan.js');
let PointCloud2 = require('./PointCloud2.js');
let PointCloud = require('./PointCloud.js');
let NavSatFix = require('./NavSatFix.js');
let BatteryState = require('./BatteryState.js');

module.exports = {
  LaserEcho: LaserEcho,
  MagneticField: MagneticField,
  CameraInfo: CameraInfo,
  TimeReference: TimeReference,
  Temperature: Temperature,
  PointField: PointField,
  Range: Range,
  MultiDOFJointState: MultiDOFJointState,
  Joy: Joy,
  RegionOfInterest: RegionOfInterest,
  Imu: Imu,
  NavSatStatus: NavSatStatus,
  JointState: JointState,
  JoyFeedbackArray: JoyFeedbackArray,
  FluidPressure: FluidPressure,
  ChannelFloat32: ChannelFloat32,
  JoyFeedback: JoyFeedback,
  Image: Image,
  RelativeHumidity: RelativeHumidity,
  LaserScan: LaserScan,
  Illuminance: Illuminance,
  CompressedImage: CompressedImage,
  MultiEchoLaserScan: MultiEchoLaserScan,
  PointCloud2: PointCloud2,
  PointCloud: PointCloud,
  NavSatFix: NavSatFix,
  BatteryState: BatteryState,
};
