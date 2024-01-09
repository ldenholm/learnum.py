# Types of data continuous / discrete

Continuous data may appear to be discrete because of representing real numbers on a computer (aka rounding) but typically any data stored as a float is considered continuous.

Categorical data e.g. gender, blood type, fruits.
Sub types of categorical data:
- Nominal = no inherent order to the categories.
- Ordinal = categories have order.

Loose examples, nominal could be eye color. Ordinal could be education level, there is some inherent heirarchy (ordering) in the data for example a masters degree is higher than completing primary school.

Time series data captured via at frequent time segments where time is crucial to the dataset.

Cross sectional data a snapshot of a population/sample at a specific moment. E.g. surveys of a population for some data points would yield cross sectional data.

Longitudinal data tracks the same subjects over multiple time points. It differs from time series in that it's not captured at regular intervals, instead it's recorded at key moments. Example education cohort study or clinical trials.

Panel data combines longitudinal and cross sectional data, often used in economics and finance. Panel data is best represented in higher dimension (3 space rather than 2 space).

Binary data includes yes/no responses, success/failures. Sort of like Bernoulli trials.

Geospatial data associated with specific geographic locations. Typically comprised of GPS coords, countour maps, climate data indexed by region.

Image and Video data consist of pixels and represent digitized images.

## Models

Dependent: values thought to depend on independent variables (output). Usually f(x_i) for x_i inputs.
Independent: values which are independent of the dependent variables (inputs).

Types of models:
- Regression: Predicting a numerical outcome.
- Classification: Predicting a categorical outcome or class.
- Clustering: Grouping similar data points together.
- Dimensionality Reduction: Reducing the complexity of high dimensional data by representing it in a lower dimensional space.

Types of learning: Supervised, Unsupervised.
Supervised learning occurs when we have all the label information required to make predictions. Unsupervised occurs when we wish to discover patterns in data without the associated labels.