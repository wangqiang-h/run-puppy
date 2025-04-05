<template>
    <div class="main-container">
      <div class="top-navigation">
        <div class="status-bar">
          <div class="left-side">
            <div class="status-bar-time"><span class="time">9:41</span></div>
          </div>
          <div class="dynamic-island">
            <div class="status-bar-dynamic-island">
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
      <div class="frame">
        <div class="magnifier"></div>
        <span class="search-here">Search here</span>
      </div>
      <span class="results-week">Results of the week</span>
      <div class="rectangle">
        <div class="flex-row-b">
          <span class="mon">mon</span><span class="tue">tue</span
          ><span class="wed">wed</span><span class="thu">thu</span
          ><span class="fri">fri</span><span class="sat">sat</span
          ><span class="sun">sun</span>
        </div>
        <div class="flex-row-c">
          <div class="ellipse"></div>
          <div class="ellipse-1"></div>
          <div class="ellipse-2"></div>
          <div class="ellipse-3"></div>
          <div class="ellipse-4"></div>
          <div class="ellipse-5"></div>
          <div class="ellipse-6"></div>
        </div>
      </div>
      <div class="pinterest-download" @click="goVIP">
        <div class="rectangle-7">
          <span class="club-vip">成为<br />俱乐部vip</span>
        </div>
        <div class="rectangle-8"><span class="join-member">加入会员</span></div>
      </div>
      <div class="message-alert"></div>
      <div class="logo"></div>
      <span class="pet">pet</span>
      <div class="frame-9">
        <span class="recommendation">Recommendation</span>
        <div class="frame-a">
          <div class="frame-b">
            <div class="frame-c">
              <div class="img-9"></div>
              <div class="frame-d">
                <span class="siamese-cat">Siamese Cat</span
                ><span class="price">$123,00</span>
              </div>
              <div class="frame-e">
                <div class="star"></div>
                <span class="rating">4.7</span>
              </div>
            </div>
            <div class="frame-f">
              <div class="section"></div>
              <div class="frame-10">
                <span class="siamese-cat-11">Siamese Cat</span
                ><span class="price-12">$123,00</span>
              </div>
              <div class="frame-13">
                <div class="star-14"></div>
                <span class="rating-15">4.7</span>
              </div>
            </div>
          </div>
          <div class="frame-16">
            <div class="frame-17">
              <div class="download-section"></div>
              <div class="frame-18">
                <span class="siamese-cat-19">Siamese Cat</span
                ><span class="price-1a">$123,00</span>
              </div>
              <div class="frame-1b">
                <div class="star-1c"></div>
                <span class="rating-1d">4.7</span>
              </div>
            </div>
            <div class="frame-1e">
              <div class="pinterest-download-1f"></div>
              <div class="frame-20">
                <span class="siamese-cat-21">Siamese Cat</span
                ><span class="price-22">$123,00</span>
              </div>
              <div class="frame-23">
                <div class="star-24"></div>
                <span class="rating-25">4.7</span>
              </div>
            </div>
          </div>
        </div>
        <span class="see-all">See All</span>
      </div>
      <div class="home-indicator"></div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';

const router = useRouter();

const goVIP = () => {
  router.push({ name: 'vip' });
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
  background: #ffffff;
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
  background: #ffffff;
  z-index: 70;
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
  z-index: 71;
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
  z-index: 72;
}
.status-bar-time {
  flex-shrink: 0;
  position: relative;
  width: 54px;
  height: 21px;
  z-index: 73;
  border-radius: 24px;
}
.time {
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
  z-index: 74;
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
  z-index: 75;
}
.status-bar-dynamic-island {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 76;
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
  z-index: 77;
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
  z-index: 78;
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
  z-index: 79;
}
.signal-wifi-battery {
  display: flex;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8px;
  position: relative;
  width: 78.401px;
  z-index: 80;
}
.icon-mobile-signal {
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 12px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/mobile-signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 81;
}
.wifi {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 82;
}
.status-bar-battery {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 83;
}
.frame {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 10.342px;
  position: relative;
  width: 355.761px;
  height: 55.846px;
  margin: 73.427px 0 0 20px;
  padding: 14.479px 17.581px 14.479px 17.581px;
  background: #f2f5f7;
  z-index: 2;
  overflow: hidden;
  border-radius: 27.923px;
}
.magnifier {
  flex-shrink: 0;
  position: relative;
  width: 26.889px;
  height: 26.889px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/magnifier-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 3;
  overflow: hidden;
}
.search-here {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 95px;
  height: 20px;
  color: #d4d4d4;
  font-family: Inter, var(--default-font-family);
  font-size: 16.547008514404297px;
  font-weight: 500;
  line-height: 20px;
  text-align: center;
  white-space: nowrap;
  z-index: 4;
}
.results-week {
  display: block;
  position: relative;
  height: 22px;
  margin: 15.513px 0 0 20px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 18.00165367126465px;
  font-weight: 600;
  line-height: 21.786px;
  text-align: left;
  white-space: nowrap;
  z-index: 28;
}
.rectangle {
  position: relative;
  width: 355.761px;
  height: 65.154px;
  margin: 7.992px 0 0 20px;
  background: #ffe99b;
  z-index: 7;
  overflow: visible auto;
  border-radius: 14px;
}
.flex-row-b {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 249.59px;
  height: 11px;
  margin: 17.581px 0 0 53.778px;
  z-index: 14;
}
.mon {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 22px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 8;
}
.tue {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 19px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 9;
}
.wed {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 22px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 10;
}
.thu {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 20px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 11;
}
.fri {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 14px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 12;
}
.sat {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 13;
}
.sun {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 20px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 14;
}
.flex-row-c {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 243.034px;
  height: 15.513px;
  margin: 4.513px 0 0 57.915px;
  z-index: 21;
}
.ellipse {
  flex-shrink: 0;
  position: relative;
  width: 15.513px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/ellipse-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 15;
  border-radius: 50%;
}
.ellipse-1 {
  flex-shrink: 0;
  position: relative;
  width: 14.479px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/ellipse-1-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 16;
}
.ellipse-2 {
  flex-shrink: 0;
  position: relative;
  width: 15.513px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/ellipse-2-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 17;
  border-radius: 50%;
}
.ellipse-3 {
  flex-shrink: 0;
  position: relative;
  width: 15.513px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/ellipse-3-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 18;
  border-radius: 50%;
}
.ellipse-4 {
  flex-shrink: 0;
  position: relative;
  width: 15.513px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/ellipse-4-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 19;
  border-radius: 50%;
}
.ellipse-5 {
  flex-shrink: 0;
  position: relative;
  width: 14.479px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/ellipse-5-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 20;
}
.ellipse-6 {
  flex-shrink: 0;
  position: relative;
  width: 15.513px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/ellipse-6-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 21;
  border-radius: 50%;
}
.pinterest-download {
  position: relative;
  width: 355.761px;
  height: 85.838px;
  margin: 8.273px 0 0 20px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/pinterest-download-bg.png)
    no-repeat center;
  background-size: cover;
  z-index: 23;
  border-radius: 14px;
}
.rectangle-7 {
  position: absolute;
  width: 100.316px;
  height: 58.949px;
  top: 13.444px;
  left: 97.214px;
  background: #fcfdff;
  z-index: 24;
  border-radius: 13.444px;
}
.club-vip {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  width: 87px;
  height: 38px;
  top: 10.342px;
  left: 10.342px;
  color: #111b27;
  font-family: JingNanYuanMoT, var(--default-font-family);
  font-size: 18.735557556152344px;
  font-weight: 900;
  line-height: 19.335px;
  text-align: left;
  text-transform: capitalize;
  z-index: 25;
}
.rectangle-8 {
  position: absolute;
  width: 69.291px;
  height: 31.026px;
  top: 27.923px;
  left: 267.855px;
  background: #ff5218;
  z-index: 26;
  border-radius: 8.274px;
}
.join-member {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 15px;
  top: 8.273px;
  left: 9.308px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 12.774243354797363px;
  font-weight: 900;
  line-height: 15px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 27;
}
.message-alert {
  position: absolute;
  width: 62.051px;
  height: 62.051px;
  top: 59px;
  left: 320.949px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/message-alert-icon.svg)
    no-repeat center;
  background-size: cover;
  overflow: hidden;
}
.logo {
  position: absolute;
  width: 36.197px;
  height: 40.334px;
  top: 70.376px;
  left: 22.068px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/pet-logo.svg)
    no-repeat center;
  background-size: cover;
  z-index: 68;
  overflow: hidden;
}
.pet {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 47.574px;
  height: 33.095px;
  top: 73.479px;
  left: 66.538px;
  color: #000000;
  font-family: Tsukushi B Round Gothic, var(--default-font-family);
  font-size: 32.80961608886719px;
  font-weight: 400;
  line-height: 32.81px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 69;
  -webkit-text-stroke: 1.367px #000000;
}
.frame-9 {
  display: flex;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 158.231px;
  position: absolute;
  width: 355.761px;
  height: 550.188px;
  top: 415.795px;
  left: 20px;
  z-index: 29;
}
.recommendation {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-basis: auto;
  position: relative;
  width: 153px;
  height: 22px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 18.00165367126465px;
  font-weight: 600;
  line-height: 21.786px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 30;
}
.frame-a {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 17.581px;
  position: relative;
  width: 355.761px;
  z-index: 32;
}
.frame-b {
  display: flex;
  align-items: center;
  justify-content: space-between;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  z-index: 33;
}
.frame-c {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8.274px;
  position: relative;
  width: 173.744px;
  z-index: 34;
}
.img-9 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 186.154px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/siamese-cat-image.png)
    no-repeat center;
  background-size: cover;
  z-index: 35;
  border-radius: 22.752px;
}
.frame-d {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 4.137px;
  position: relative;
  min-width: 0;
  height: 51.709px;
  padding: 7.239px 0 7.239px 0;
  z-index: 36;
}
.siamese-cat {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 37;
}
.price {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #f96a36;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 38;
}
.frame-e {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: absolute;
  width: 55.846px;
  height: 25.855px;
  top: 10.342px;
  left: 105.487px;
  padding: 2.068px 7.239px 2.068px 7.239px;
  background: #ffffff;
  z-index: 39;
  overflow: hidden;
  border-radius: 12.927px;
}
.star {
  flex-shrink: 0;
  position: relative;
  width: 17.582px;
  height: 17.582px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/star-rating-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 40;
  border-radius: 0.52px;
}
.rating {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 16px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 13.499946594238281px;
  font-weight: 500;
  line-height: 16px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 41;
}
.frame-f {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8.274px;
  position: relative;
  width: 173.744px;
  z-index: 42;
}
.section {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 186.154px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/cat-product-image.png)
    no-repeat center;
  background-size: cover;
  z-index: 43;
  border-radius: 22.752px;
}
.frame-10 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 4.137px;
  position: relative;
  min-width: 0;
  height: 51.709px;
  padding: 7.239px 0 7.239px 0;
  z-index: 44;
}
.siamese-cat-11 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 45;
}
.price-12 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #f96a36;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 46;
}
.frame-13 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: absolute;
  width: 55.846px;
  height: 25.855px;
  top: 10.342px;
  left: 105.487px;
  padding: 2.068px 7.239px 2.068px 7.239px;
  background: #ffffff;
  z-index: 47;
  overflow: hidden;
  border-radius: 12.927px;
}
.star-14 {
  flex-shrink: 0;
  position: relative;
  width: 17.582px;
  height: 17.582px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/star-rating-icon-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 48;
  border-radius: 0.52px;
}
.rating-15 {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 16px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 13.499946594238281px;
  font-weight: 500;
  line-height: 16px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 49;
}
.frame-16 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  z-index: 50;
}
.frame-17 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8.274px;
  position: relative;
  width: 173.744px;
  z-index: 51;
}
.download-section {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 186.154px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/pet-product-image-3.png)
    no-repeat center;
  background-size: cover;
  z-index: 52;
  border-radius: 22.752px;
}
.frame-18 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 4.137px;
  position: relative;
  min-width: 0;
  height: 51.709px;
  padding: 7.239px 0 7.239px 0;
  z-index: 53;
}
.siamese-cat-19 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 54;
}
.price-1a {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #f96a36;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 55;
}
.frame-1b {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: absolute;
  width: 55.846px;
  height: 25.855px;
  top: 10.342px;
  left: 105.487px;
  padding: 2.068px 7.239px 2.068px 7.239px;
  background: #ffffff;
  z-index: 56;
  overflow: hidden;
  border-radius: 12.927px;
}
.star-1c {
  flex-shrink: 0;
  position: relative;
  width: 17.582px;
  height: 17.582px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/star-rating-icon-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 57;
  border-radius: 0.52px;
}
.rating-1d {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 16px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 13.499946594238281px;
  font-weight: 500;
  line-height: 16px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 58;
}
.frame-1e {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8.274px;
  position: relative;
  width: 173.744px;
  z-index: 59;
}
.pinterest-download-1f {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 186.154px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/pet-product-image-4.png)
    no-repeat center;
  background-size: cover;
  z-index: 60;
  border-radius: 22.752px;
}
.frame-20 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 4.137px;
  position: relative;
  min-width: 0;
  height: 51.709px;
  padding: 7.239px 0 7.239px 0;
  z-index: 61;
}
.siamese-cat-21 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 62;
}
.price-22 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #f96a36;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 63;
}
.frame-23 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: absolute;
  width: 55.846px;
  height: 25.855px;
  top: 10.342px;
  left: 105.487px;
  padding: 2.068px 7.239px 2.068px 7.239px;
  background: #ffffff;
  z-index: 64;
  overflow: hidden;
  border-radius: 12.927px;
}
.star-24 {
  flex-shrink: 0;
  position: relative;
  width: 17.582px;
  height: 17.582px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/185010/star-rating-icon-4.svg)
    no-repeat center;
  background-size: cover;
  z-index: 65;
  border-radius: 0.52px;
}
.rating-25 {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 16px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 13.499946594238281px;
  font-weight: 500;
  line-height: 16px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 66;
}
.see-all {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-basis: auto;
  position: relative;
  width: 44px;
  height: 16px;
  color: #b7b7b7;
  font-family: Inter, var(--default-font-family);
  font-size: 13.346052169799805px;
  font-weight: 500;
  line-height: 16px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 31;
}
.home-indicator {
  position: absolute;
  height: 5px;
  right: 129px;
  bottom: 8px;
  left: 130px;
  background: #000000;
  z-index: 85;
  border-radius: 100px;
}

</style>
  