# End-to-End Regression Model Pipeline Development with FastAPI: From Data Scraping to Deployment with CI/CD Integration"

Click on the image to see full view.
<table style="width:100%">
<tr>
  <td><img src="https://i.imgur.com/n8tEwXy.png" alt="Image" width="550px" height=260px/></td>
  <td><img src="https://i.imgur.com/ErYjDFz.png" alt="Image" width="550px" height=260px/></td>
  </tr>
</table>

# Section 1: Research and Development

The project is a comprehensive end-to-end solution for real estate data analysis and machine learning model deployment. It starts with the collection of real estate data from a website, which is then processed and cleaned to ensure data quality and consistency. The scrapped data is uploaded to [Kaggle](https://www.kaggle.com/datasets/mazhar01/real-state-website-data). [Github repo](https://github.com/mm-mazhar/Scraping-Zameen.com). The cleaned data is further analyzed and features are engineered using popular libraries such as pandas, numpy, SK-Learn and Feature Engine, which involves little bit of changes in sci-kit learn classes and build a pipeline for Research and Development Phase.

Click on the image to see full view.
<table style="width:100%; align=center">
<tr>
  <td><img src="https://i.imgur.com/tFl5pxt.png" /></td>
  <!-- <td><img src="https://i.imgur.com/hBVPlLm.png" alt="Image" width="560px" height=260px/></td> -->
</tr>
</table>

# Section 2: Production Model Package

The next phase involves building a robust ML pipeline, where the Lasso Regression Model is trained and fine-tuned using the processed data. The model is packaged and uploaded to [PyPi](https://pypi.org/project/lasso-regression-model/) to ensure easy integration and deployment. The packaging process includes organizing dependencies, and creating a reproducible environment.

The project follows software engineering practices, with an emphasis on testing using Pytest and Tox. Pytest provides a comprehensive testing framework that allows for thorough testing of individual components, ensuring the reliability and correctness of the system. Tox, on the other hand, facilitates testing across different environments and configurations, enabling comprehensive and reliable test coverage.

Click on the image to see full view.
<table style="width:100%; align=center">
<tr>
  <td><img src="https://i.imgur.com/LaKEGVc.png" alt="Image" width="570px" height=180px/></td>
  <td><img src="https://i.imgur.com/o6lW6XL.png" alt="Image" width="570px" height=180px/></td>
  <td><img src="https://i.imgur.com/7KNhQdl.png" alt="Image" width="570px" height=180px/></td>
</tr>
</table>

# Section 3: Model Serving API (FastAPI)

To expose the trained machine learning model as API, the project utilizes FastAPI, a modern and efficient web framework. This allows users to send requests to the deployed model and receive predictions or valuable insights based on the real estate data.

[Link to Deloyed API](https://tame-hook-production.up.railway.app/docs#/default/predict_api_v1_predict_post)

Click on the image to see full view.
<table style="width:100%; align=center">
<tr>
  <td><img src="https://i.imgur.com/5yARjOK.png"/></td>
  </tr>
</table>

# Section 4: CI/CD (CircleCI)

Continuous integration and deployment are achieved through the use of CircleCI, a popular CI/CD platform. This enables automated building, testing, and deployment of the machine learning models, ensuring a streamlined and efficient development process.

Click on the image to see full view.
<table style="width:100%; align=center">
<tr>
  <td><img src="https://i.imgur.com/6VgrYDU.png" alt="Image" width="570px" height=170px/></td>
  <td><img src="https://i.imgur.com/W30TQs5.png" alt="Image" width="570px" height=170px/></td>
  <td><img src="https://i.imgur.com/zqXTSkz.png" alt="Image" width="570px" height=170px/></td>
  <td><img src="https://i.imgur.com/8dHAlyd.png" alt="Image" width="570px" height=170px/></td>
</tr>
</table>

# Section 5: Deploying with Containers (Docker)

Click on the image to see full view.
<table style="width:100%; align=center">
<tr>
  <td><img src="https://i.imgur.com/4MSniph.png" /></td>
</tr>
</table>

Overall, the project showcases a comprehensive approach to real estate data analysis and model deployment, combining data scraping, data processing, feature engineering, machine learning, API development, and CI/CD practices. It provides a scalable and efficient solution for real estate professionals and stakeholders to gain valuable insights and make data-driven decisions in the dynamic real estate market.