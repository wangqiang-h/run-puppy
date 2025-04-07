<template>
    <div class="main-container">
      <div class="top-navigation">
        <div class="status-bar">
          <div class="left-side">
            <div class="status-bar-time"><span class="edit-time">9:41</span></div>
          </div>
          <div class="dynamic-island">
            <div class="status-bar-1">
              <div class="true-depth-camera"></div>
              <div class="facetime-camera"></div>
            </div>
          </div>
          <div class="right-side">
            <div class="signal-wifi-battery">
              <div class="icon-mobile-signal"></div>
              <div class="wifi"></div>
              <div class="status-bar-battery"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="frame"><div class="vector" @click="goToRunningHome"></div></div>
      <div class="flex-row-ad">
        <div class="frame-2"><span class="calorie">卡路里：0.0</span></div>
        <div class="frame-3"><span class="kilometer">公里：0.0</span></div>
      </div>
      <div class="empty"></div>
      <div class="frame-4">
        <div class="frame-5"><div class="fi-sr-paw"></div></div>
        <span class="get-started" @click="goToRunningHome">get started</span>
      </div>
      <div class="home-indicator"></div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';

const router = useRouter();

const goToRunningHome = () => {
  router.push({ name: 'running_home' });
};
</script>
  
  <style scoped>
:root {
  --default-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Ubuntu, "Helvetica Neue", Helvetica, Arial, "PingFang SC",
    "Hiragino Sans GB", "Microsoft Yahei UI", "Microsoft Yahei",
    "Source Han Sans CN", sans-serif;
}

.main-container {
  overflow: hidden;
}

.main-container,
.main-container * {
  box-sizing: border-box;
}

input,
select,
textarea,
button {
  outline: 0;
}

.main-container {
  position: relative;
  width: 393px;
  height: 852px;
  margin: 0 auto;
  background: linear-gradient(180deg, #fffbd7, #fffefe);
  overflow: hidden;
}
.top-navigation {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 2px;
  position: relative;
  width: 393px;
  margin: 0 0 0 0;
  backdrop-filter: blur(10px);
}
.status-bar {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 59px;
  z-index: 1;
}
.left-side {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 0 3px 10px;
  z-index: 2;
}
.status-bar-time {
  flex-shrink: 0;
  position: relative;
  width: 54px;
  height: 21px;
  z-index: 3;
  border-radius: 24px;
}
.edit-time {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 54px;
  height: 20px;
  top: 1px;
  left: 0;
  color: #000000;
  font-family: SF Pro Text, var(--default-font-family);
  font-size: 16px;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
  white-space: nowrap;
  letter-spacing: -0.32px;
  z-index: 4;
}
.dynamic-island {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  width: 125px;
  min-height: 0;
  z-index: 5;
}
.status-bar-1 {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 6;
  border-radius: 100px;
}
.true-depth-camera {
  position: absolute;
  width: 80px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(-78.13%, -50%);
  z-index: 7;
  overflow: hidden;
  border-radius: 100px;
}
.facetime-camera {
  position: absolute;
  width: 37px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(68.92%, -50%);
  z-index: 8;
  overflow: hidden;
  border-radius: 100px;
}
.right-side {
  display: flex;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 11px 0 0;
  z-index: 9;
}
.signal-wifi-battery {
  display: flex;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8px;
  position: relative;
  width: 78.401px;
  z-index: 10;
}
.icon-mobile-signal {
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 12px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/201739/mobile-signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.wifi {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/201739/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.status-bar-battery {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/201739/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.frame {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: relative;
  width: 51px;
  height: 51px;
  margin: 22px 0 0 30px;
  padding: 19px 21px 19px 21px;
  background: #ffe99b;
  z-index: 25;
  border-radius: 25.5px;
}
.vector {
  flex-shrink: 0;
  position: relative;
  width: 11px;
  height: 15px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/201739/vector-arrow.svg)
    no-repeat center;
  background-size: cover;
  z-index: 26;
}
.flex-row-ad {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 334px;
  height: 42px;
  margin: 15px 0 0 30px;
  z-index: 22;
}
.frame-2 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 162px;
  height: 42px;
  padding: 17px 33px 17px 33px;
  background: #000000;
  z-index: 20;
  border-radius: 43.5px;
}
.calorie {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 114px;
  height: 25px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20.448429107666016px;
  font-weight: 600;
  line-height: 24.747px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 21;
}
.frame-3 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 162px;
  height: 42px;
  padding: 17px 33px 17px 33px;
  background: #000000;
  z-index: 22;
  border-radius: 43.5px;
}
.kilometer {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 94px;
  height: 25px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20.448429107666016px;
  font-weight: 600;
  line-height: 24.747px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 23;
}
.empty {
  position: relative;
  width: 206px;
  height: 240px;
  margin: 141px 0 0 111px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/201739/empty-state-image.png)
    no-repeat center;
  background-size: cover;
  z-index: 24;
}
.frame-4 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 65px;
  position: relative;
  width: 334px;
  height: 59px;
  margin: 158px 0 0 30px;
  padding: 5px 6px 5px 6px;
  background: #ff5218;
  z-index: 16;
  border-radius: 29.5px;
}
.frame-5 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 75px;
  height: 48px;
  padding: 13px 27px 13px 27px;
  background: #000000;
  z-index: 17;
  border-radius: 24px;
}
.fi-sr-paw {
  flex-shrink: 0;
  position: relative;
  width: 21px;
  height: 21px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/201739/paw-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 18;
  overflow: hidden;
}
.get-started {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 114px;
  height: 25px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20.448429107666016px;
  font-weight: 500;
  line-height: 24.747px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 19;
}
.home-indicator {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 52px 0 0 130px;
  background: #000000;
  z-index: 15;
  border-radius: 100px;
}

</style>
  